import hashlib
import uuid
import re
import json
from collections import OrderedDict

import numpy as np


class TrajectoryData(object):
    """Tabular data of expectation values for one or more trajectories.
    Multiple TrajectoryData objects can be combined with the `extend` method,
    in order to accumulate averages over an arbitrary number o trajectories. As
    much as possible, it is checked that all trajectories are statistically
    independent. A record is kept to ensure exact reproducability.

    :attribute ID: A unique ID for the current state of the TrajectoryData
        (read-only). See property documentation below
    :type ID: str
    :attribute table: A table (OrderedDict of column names to numpy arrays)
        that contains four column for every known operator (real/imaginary
        part of the expectation value, real/imaginary part of the variance).
        Note that the `table` attribute can easily be converted to a pandas
        DataFrame (``DataFrame(data=traj.table)``). The `table` attribute
        should be considered read-only.
    :type table: OrderedDict(str) => numpy array
    :attribute dt: Time step between data points
    :type dt: float
    :attribute nt: Number of time steps / data points
    :type nt: int
    :attribute operators: An iterator of the operator names. The column names
        in the `table` attribute derive from these. Assuming "X" is one of the
        operator names, there will be four keys in `table`:
       "Re[<X>]", "Im[<X>]", "Re[var(X)]", "Im[var(X)]"
    :type operators: list of str
    :attribute record: A copy of the complete record of how the averaged
        expectation values for all operators were obtained. See indepth
        discussion in the property documentation below.
    :type record: OrderedDic(str) => tuple(int, int, list)
    :attribute col_width: width of the data columns when writing out data.
        Defaults to 25 (allowing to full double precision). Note that
        operator names may be at most of length `col_width-10`
    :type col_width: int
    """
    # When instantiating with the from_qsd_data class method, we want the
    # ID to depend uniquely on the read data files (via their md5 hash).
    # RFC4122 accounts for a situation like this with a "UUID3" that requires
    # the combination of a namespace and a name. We define a completely
    # arbitrary namespace UUID here for this purpose.
    _uuid_namespace = uuid.UUID('c84069eb-cf80-48a6-9584-74b7f2c742c1')
    _prec_dt = 1.0e-6 # how close dt's have to be to be equal
    col_width = 25 # width of columns when writing
    _rx_op_name = re.compile(r'^[\x20-\x7E]+$') # ascii w/o control chars

    def __init__(self, ID, dt, seed, n_trajectories, data):
        """Initialize a new TrajectoryData instance

        :param ID: A unique, RFC 4122 compliant identifier (as generated by the
            `new_id` class method)
        :type ID: str
        :param dt: Time step between data points (>0)
        :type dt: float
        :param seed: The random number generator seed on which the data is
            based
        :type seed: int
        :param n_trajectories: The number of trajectories from which the data
            is averaged (It is assumed that the random number generator was
            seeded with the given seed, and then the given number of
            trajectories were calculated *sequentially*)
        :type n_trajectories: int
        :param data: dictionary (preferably OrderedDict) of expectation value
            data. The value of `data[operator_name]` must be a tuple of four
            numpy arrays (real part of expectation value, imaginary part of
            expectation value, real part of standard deviation, imaginary part
            of standard deviation). The operator names must contain only ASCII
            characters and must be shorter than `col_width - 10`.
        :type data: dict(str) => tuple of arrays

        :raises ValueError: if `ID` is not RFC 4122 compliant, `dt` is an
            invalid or non-positive float, data does not follow the correct
            structure
        """
        self._ID = str(uuid.UUID(ID)) # self.ID = ID, with validation
        self.table = OrderedDict()
        self._dt = float(dt)
        if self.dt <= 0.0:
            raise ValueError("dt must be a value >0")
        self._operators = []
        for op, (re_exp, im_exp, re_var, im_var) in data.items():
            op = str(op)
            if len(op) > (self.col_width - 10):
                raise ValueError(("Operator name '%s' supersedes maximum "
                                 "length of %d") % (op, self.col_width-10))
            if not self._rx_op_name.match(op):
                raise ValueError(("Operator name '%s' contains invalid "
                                  "characters") % op)
            self._operators.append(op)
            self._nt = len(re_exp) # assumed valid for all (check below)
            re_exp_lb, im_exp_lb, re_var_lb, im_var_lb \
            = self._operator_cols(op)
            self.table[re_exp_lb] = np.array(re_exp, dtype=np.float64)
            self.table[im_exp_lb] = np.array(im_exp, dtype=np.float64)
            self.table[re_var_lb] = np.array(re_var, dtype=np.float64)
            self.table[im_var_lb] = np.array(im_var, dtype=np.float64)
        for col in self.table:
            if len(self.table[col]) != self.nt:
                raise ValueError("All columns must be of length nt")
        record_ops = self._operators.copy()
        self._record = OrderedDict([
                         (self.ID, (seed, n_trajectories, record_ops)),
                       ])

    def __eq__(self, other):
        return self.ID == other.ID

    def __hash__(self):
        return hash(self.ID)

    def copy(self):
        """Return a (deep) copy of the current object"""
        data = OrderedDict()
        for op in self._operators:
            cols = self._operator_cols(op)
            data[op] = tuple([self.table[col] for col in cols])
        new = self.__class__(ID=self.ID, dt=self.dt, seed=None,
                             n_trajectories=None, data=data)
        new._record = self._record.copy()
        return new

    @staticmethod
    def _operator_cols(op):
        """Return the four column names holding the data for the given
        operator"""
        return ['Re[<'+op+'>]', 'Im[<'+op+'>]',
                'Re[var('+op+')]', 'Im[var('+op+')]']

    @classmethod
    def read(cls, filename):
        """Read in TrajectoryData from the given filename. The file must be in
        the format generated by the `write` method"""
        raise NotImplementedError()

    @classmethod
    def from_qsd_data(cls, operators, seed):
        """Instantiate from one or more QSD output files specified as values of
        the dictionary `operators`

        Each QSD output file must have the following structure:
        * The first line must start with the string "Number_of_Trajectories",
          followed by an integer (separated by whitespace)
        * All following lines must contain five floating point numbers
          (time, real/imaginary part of expectation value, and real/imaginary
          part of variance), separated by whitespace.

        All QSD output files must contain the same number of lines, specify the
        same number of trajectories, and use the same time grid values (first
        column). It is the user's responsibility to ensure that all out output
        files were indeed generated in a single QSD run using the specified
        initial seed for the random number generator.

        :param operators: dictionary (preferrably OrderedDict) of operator
            name to filename. Each filename must contain data in the format
            described above
        :type operators: dict(str) => str
        :param seed: The seed to the random number generator that was used to
            produce the data file
        :type seed: int

        :raises ValueError: if any of the datafiles do not have the correct
            format or are inconsistent

        Note: Remember that is is vitally important that all
        quantum trajectories that go into an average are statistically
        independent. The TrajectoryData class tries as much as possible to
        ensure this, by refusing to combine indentical IDs, or trajectories
        originating from the same seed. To this end, in the `from_qsd_data`
        method, the ID of the instantiated object will depend uniquely on the
        collective data read from the QSD output files."""
        md5s = [] # MD5 hash of all files (in order to generate ID)
        data = OrderedDict();
        n_trajectories = None
        dt = None
        if len(operators) == 0:
            raise ValueError("Must give at least one mapping "
                             "operator_name => file in operators dic")
        for (operator_name, file_name) in operators.items():
            md5s.append(hashlib.md5(open(file_name,'rb').read()).hexdigest())
            with open(file_name) as in_fh:
                header = in_fh.readline()
                m = re.match(r'Number_of_Trajectories\s*(\d+)', header)
                if m:
                    file_n_trajectories = int(m.group(1))
                else:
                    raise ValueError(("First line in %s must contain the "
                                      "Number_of_Trajectories")%file_name)
            (tgrid, re_exp, im_exp, re_var, im_var) \
            = np.genfromtxt(file_name, dtype=np.float64, skip_header=1,
                            unpack=True)
            data[operator_name] = (re_exp, im_exp, re_var, im_var)
            if len(tgrid) < 2:
                raise ValueError(("File %s does not contain sufficient "
                                  "data (at least two rows)") % file_name)
            file_dt = tgrid[1] - tgrid[0]
            if dt is None:
                dt = file_dt
            else:
                if abs(dt-file_dt) > cls._prec_dt:
                    raise ValueError(("dt in file %s inconsistent with dt "
                                      "in other files")%file_name)
            if n_trajectories is None:
                n_trajectories = file_n_trajectories
            else:
                if n_trajectories != file_n_trajectories:
                    raise ValueError(("number of trajectories in file %s "
                                      "does not match number of trajectories "
                                      "in other files")%file_name)
        ID = cls.new_id(name="".join(sorted(md5s)))
        return cls(ID, dt, seed, n_trajectories, data)

    @classmethod
    def new_id(cls, name=None):
        """Generate a new unique identifier, as a string. The identifier will
        be RFC 4122 compliant. If name is None, the resulting ID will be
        random. Otherwise, name must be a string that the ID will depend on.
        That is, calling `new_id` repeatedly with the same `name` will
        result in identical IDs.
        """
        if name is None:
            return str(uuid.uuid4())
        else:
            return str(uuid.uuid3(cls._uuid_namespace, name))

    @property
    def ID(self):
        """A unique RFC 4122 complient identifier. The identifier changes
        whenever the class data is modified (via the `extend` method). Two
        instances of TrajectoryData with the same ID are assumed to be
        identical
        """
        return self._ID

    @property
    def record(self):
        """A copy of the full trajectory record, i.e. a history of calls to the
        `extend` method. Its purpose is to ensure that the data is completely
        reproducible. This entails storing the seed to the random number
        generator for all sets of trajectories.

        The record is an OrderedDict that maps the original ID of any
        TrajectoryData instance combined via `extend` to a tuple ``(seed,
        n_trajectories, ops)``, where ``seed`` is the seed to the random number
        generator that was used to calculate a specific set of trajectories
        (sequentially), ``n_trajectories`` are the number of trajectories in
        that dataset, and ``ops`` is a list of operator names for which
        expectation values were calculated. This may be the complete list of
        operators in the `operators` attribute, or a subset of those operators
        (Not all trajectories have to include data for all operators).

        For example, let's assume we have used the ``QSDCodeGen`` class to
        set up a QSD propagation. Two observables 'X1', 'X2', have been set up
        to be written to file 'X1.out', and 'X2.out'. The
        `QSDCodeGen.set_trajectories` method has been called with
        `n_trajectories=10`, after which a call to `QSDCodeGen.run` with
        argument `seed=SEED1`, performed a sequential propagation of 10
        trajectories, with the averaged expectation values written to the
        output files.

        This data may now be read into a new `TrajectoryData` instance `traj`
        via the `from_qsd_data` class method (with `seed=SEED1`). The newly
        created instance (with, let's say, ``ID='8d102e4b-...'``) will have one
        entry in its record:

            '8d102e4b-...': (SEED1, 10, ['X1', 'X2'])

        Now, let's say we add a new observable 'A2' (output file 'A2.out') for
        the `QSDCodeGen` (in addition to the existing observables X1, X2), and
        run the `QSDCodeGen.run` method again, with a new seed `SEED2`.
        We then update `traj` with a call such as

            traj.extend(TrajectoryData.from_qsd_data(
                {'X1':'X1.out', 'X2':'X2.out', 'A2':'A2.out'}, SEED2)

        The record will now have an additional entry, e.g.

            'd9831647-...': (SEED2, 10, ['X1', 'X2', 'A2'])

        `traj.table` will contain the averaged expectation values (average over
        20 trajectories for 'X1', 'X2', and 10 trajectories for 'A2'). The
        record tells use that to reproduce this table, 10 sequential
        trajectories starting from SEED1 must be performed for X1, X2, followed
        by another 10 trajectories for X1, X2, A2 starting from SEED2.
        """
        return self._record.copy()

    @property
    def operators(self):
        """Iterator over all operators"""
        return iter(self._operators)

    @property
    def record_IDs(self):
        """Set of all IDs in the record"""
        return set(self._record.keys())

    @property
    def dt(self):
        """Time step between data points"""
        return self._dt

    @property
    def nt(self):
        """Number of time steps / data points"""
        return self._nt

    @property
    def shape(self):
        """"Tuple (n_row, n_cols) for the data in self.table. The time grid is
        included in the column count"""
        return (self.nt, len(self.table.keys())+1)

    @property
    def record_seeds(self):
        """Set of all random number generator seeds in the record"""
        return set([seed for (seed, ntraj, op) in self._record.values()])

    @property
    def tgrid(self):
        """Time grid, as numpy array"""
        return np.array(range(self.nt)) * self._dt

    def operator_record(self, operator_name):
        """Returns a list of tuples (seed, n_trajectories) that specify how the
        current expectation values for the given operator where obtained"""
        raise NotImplementedError()

    def __str__(self):
        return self.to_str(show_rows=6)

    def __repr__(self):
        return "TrajectoryData(ID=%s)" % self.ID

    def _data_line(self, index, fmt):
        line = fmt % (self._dt*index)
        for col in self.table.keys():
            line += fmt % self.table[col][index]
        return line

    def to_str(self, show_rows=-1):
        """Generate full string represenation of TrajectoryData"""
        lines = []
        w = self.col_width
        prec = self.col_width - 9
        fmt = "%{width:d}.{prec:d}e".format(width=w, prec=prec)
        ellipsis = "...".center(w)
        lines.append("# QNET Trajectory Data ID %s" % self.ID)
        for (ID, (seed, n_traj, ops)) in self._record.items():
            if set(ops) == set(self._operators):
                lines.append("# Record %s (seed %d): %d" % (ID, seed, n_traj))
            else:
                lines.append("# Record %s (seed %d): %d %s"
                             % (ID, seed, n_traj, json.dumps(ops)))
        header = ("#%{width:d}s".format(width=w-1)) % 't'
        for col in self.table.keys():
            header += ("%{width:d}s".format(width=w)) % col
        lines.append(header)
        nt = self.nt
        if (show_rows < 0) or (show_rows >= nt):
            show_row_indices_1 = range(nt)
            show_row_indices_2 = []
        else:
            show_row_indices_1 = range(show_rows//2)
            show_row_indices_2 = range(nt - ((show_rows//2)+(show_rows%2)), nt)
            # if show_rows is odd, we show the first show_rows//2 rows, and the
            # last (show_rows//2)+1 rows.
        for i in show_row_indices_1:
            lines.append(self._data_line(i, fmt))
        if len(show_row_indices_2) > 0:
            lines.append((ellipsis * int(len(self.table)+1)).rstrip())
            for i in show_row_indices_2:
                lines.append(self._data_line(i, fmt))
        return "\n".join(lines)

    def write(self, filename):
        """Write data to a text file. The TrajectoryData may later be restored
        by the `read` class method from the same file"""
        with open(filename, 'w') as out_fh:
            out_fh.write(self.to_str())

    def n_trajectories(self, operator):
        "Return the total number of trajectories for the given operator"
        n_total = 0
        for ID, (seed, n_traj, ops) in self._record.items():
            if operator in ops:
                n_total += n_traj
        return n_total

    def extend(self, other):
        """Extend data with another Trajectory data set, averaging the
        expectation values. Equivalently to ``traj1.extend(traj2)``, the syntax
        ``traj1 += traj2`` may be used.

        :raises ValueError: if data in self and other are incompatible
        """
        err_msg = "TrajectoryData may only be extended by completely "\
                  "disjunct other TrajectoryData object"
        if not self.record_IDs.isdisjoint(other.record_IDs):
            raise ValueError("%s: Repeated ID"%err_msg)
        if not self.record_seeds.isdisjoint(other.record_seeds):
            raise ValueError("%s: Repeated seed"%err_msg)
        if not abs(self.dt - other.dt) < self._prec_dt:
            raise ValueError("Extending TrajectoryData does not match dt")
        for op in self._operators:
            if op in other._operators:
                n_self = self.n_trajectories(op)
                n_other = other.n_trajectories(op)
                for col in self._operator_cols(op):
                    self.table[col] *= n_self
                    self.table[col] += n_other * other.table[col]
                    self.table[col] /= float(n_self + n_other)
        # we may also have to account for other containing new operators
        for op in other._operators:
            if op not in self._operators:
                self._operators.append(op)
                for col in self._operator_cols(op):
                    self.table[col] = other.table[col].copy()
        self._record.update(other._record)
        self._ID = self.new_id(name="".join(sorted([self.ID, other.ID])))

    def __add__(self, other):
        combined = self.copy()
        combined.extend(other)
        return combined

    def __iadd__(self, other):
        self.extend(other)
        return self


