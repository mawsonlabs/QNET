#This file is part of QNET.
#
#    QNET is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#    QNET is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with QNET.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2012, Nikolas Tezak
#
###########################################################################


class BadPermutationError(ValueError):
    """
    Can be raised to signal that a permutation does not pass the :py:func:check_permutation test.
    """
    pass

def check_permutation(permutation):
    """
    Verify that a tuple of permutation image points ``(sigma(1), sigma(2), ..., sigma(n))``
    is a valid permutation, i.e. each number from 0 and n-1 occurs exactly once. I.e. the following **set**-equality must hold:

        ``{sigma(1), sigma(2), ..., sigma(n)} == {0, 1, 2, ... n-1}``

    :param permutation: Tuple of permutation image points
    :type permutation: tuple
    :rtype: bool
    """
    return list(sorted(permutation)) == range(len(permutation))


def invert_permutation(permutation):
    """
    Compute the image tuple of the inverse permutation.
    :param permutation: A valid (cf. :py:func:check_permutation) permutation.
    :return: The inverse permutation tuple
    :rtype: tuple
    """
    return tuple([permutation.index(p) for p in range(len(permutation))])

def permutation_to_disjoint_cycles(permutation):
    """
    Any permutation sigma can be represented as a product of cycles.
    A cycle (c_1, .. c_n) is a closed sequence of indices such that

      sigma(c_1) == c_2, sigma(c_2) == sigma^2(c_1)== c_3, ..., sigma(c_(n-1)) == c_n, sigma(c_n) == c_1

    Any single length-n cycle admits n equivalent representations in correspondence with which element one defines as c_1.

        (0,1,2) == (1,2,0) == (2,0,1)

    A decomposition into *disjoint* cycles can be made unique, by requiring that the cycles are sorted by their smallest element,
    which is also the left-most element of each cycle. Note that permutations generated by disjoint cycles commute.
    E.g.,

        (1, 0, 3, 2) == ((1,0),(3,2)) --> ((0,1),(2,3)) normal form

    :param permutation: A valid permutation image tuple
    :type permutation: tuple
    :return: A list of disjoint cycles, that when comb
    :rtype: list
    :raise: BadPermutationError
    """
    if not check_permutation(permutation):
        raise BadPermutationError('Malformed permutation %r' % permutation)

    p_index = 0
    current_cycle = [0]

    # keep track of all remaining/unvisited indices
    permutation_nums = range(1,len(permutation))


    cycles = []
    while True:
        # find next image point in cycle
        p_index = permutation[p_index]

        # if back at start of cycle
        if p_index == current_cycle[0]:

            # store cycle
            cycles.append(current_cycle)

            try:
                # retrieve the next lowest un-used image point
                p_index = permutation_nums.pop(0)
                current_cycle = [p_index]

            except IndexError:
                break
        else:
            permutation_nums.remove(p_index)
            current_cycle.append(p_index)

    return cycles

def permutation_from_disjoint_cycles(cycles, offset = 0):
    """
    Reconstruct a permutation image tuple from a list of disjoint cycles
    :param cycles: sequence of disjoint cycles
    :type cycles: list or tuple
    :param offset: Offset to subtract from the resulting permutation image points
    :type offset: int
    :return: permutation image tuple
    :rtype: tuple
    """
    perm_length = sum(map(len, cycles))
    res_perm = range(perm_length)
    for c in cycles:
        p1 = c[0] - offset
        for p2 in c[1:]:
            p2 = p2 - offset
            res_perm[p1] = p2
            p1 = p2
        res_perm[p1] = c[0] - offset #close cycle
    assert sorted(res_perm) == range(perm_length)
    return tuple(res_perm)

def permutation_to_block_permutations(permutation):
    """
    If possible, decompose a permutation into a sequence of permutations
    each acting on individual ranges of the full range of indices.
    E.g.

        ``(1,2,0,3,5,4) --> (1,2,0) [+] (0,2,1)``

    :param permutation: A valid permutation image tuple ``s = (s_0,...s_n)`` with ``n > 0``
    :type permutation: tuple
    :return: A list of permutation tuples ``[t = (t_0,...,t_n1), u = (u_0,...,u_n2),..., z = (z_0,...,z_nm)]`` such that ``s = t [+] u [+] ... [+] z``
    :rtype: list of tuples
    :raise: ValueError
    """
    if len(permutation) == 0 or not check_permutation(permutation):
        raise BadPermutationError()

    cycles = permutation_to_disjoint_cycles(permutation)

    if len(cycles) == 1:
        return (permutation,)
    current_block_start = cycles[0][0]
    current_block_end = max(cycles[0])
    current_block_cycles = [cycles[0]]
    res_permutations = []
    for c in cycles[1:]:
        if c[0] > current_block_end:
            res_permutations.append(permutation_from_disjoint_cycles(current_block_cycles, current_block_start))
            assert sum(map(len, current_block_cycles)) == current_block_end - current_block_start + 1
            current_block_start = c[0]
            current_block_end = max(c)
            current_block_cycles = [c]
        else:
            current_block_cycles.append(c)
            if max(c) > current_block_end:
                current_block_end = max(c)

    res_permutations.append(permutation_from_disjoint_cycles(current_block_cycles, current_block_start))

    assert sum(map(len, current_block_cycles)) == current_block_end - current_block_start + 1
    assert sum(map(len, res_permutations)) == len(permutation)

    return res_permutations


def permutation_from_block_permutations(permutations):
    """
    Reverse operation to :py:func:`permutation_to_block_permutations`
    Compute the concatenation of permutations

        ``(1,2,0) [+] (0,2,1) --> (1,2,0,3,5,4)``

    :param permutations: A list of permutation tuples
                                 ``[t = (t_0,...,t_n1), u = (u_0,...,u_n2),..., z = (z_0,...,z_nm)]``
    :type permutations: list of tuples
    :return: permutation image tuple
                    ``s = t [+] u [+] ... [+] z``
    :rtype: tuple
    """
    offset = 0
    new_perm = []
    for p in permutations:
        new_perm[offset: offset +len(p)] = [p_i + offset for p_i in p]
        offset += len(p)
    return tuple(new_perm)


def compose_permutations(alpha, beta):
    r"""
    Find the composite permutation

    .. math::

        \sigma := \alpha \cdot \beta \\
        \Leftrightarrow \sigma(j) = \alpha\left(\beta(j)\right) \\


    :param a: first permutation image tuple
    :type alpha: tuple
    :param beta: second permutation image tuple
    :type beta: tuple
    :return: permutation image tuple of the composition.
    :rtype: tuple
    """
    return permute(alpha, beta)

#TODO remove redundant function concatenate_permutations
def concatenate_permutations(a, b):
    """
    Concatenate two permutations:
        s = a [+] b

    :param a: first permutation image tuple
    :type a: tuple
    :param b: second permutation image tuple
    :type b: tuple
    :return: permutation image tuple of the concatenation.
    :rtype: tuple
    """
    return permutation_from_block_permutations([a, b])

def permute(sequence, permutation):
    """
    Apply a permutation sigma({j}) to an arbitrary sequence.

    :param sequence: Any finite length sequence ``[l_1,l_2,...l_n]``. If it is a list, tuple or str, the return type will be the same.
    :param permutation: permutation image tuple
    :type permutation: tuple
    :return: The permuted sequence ``[l_sigma(1), l_sigma(2), ..., l_sigma(n)]``
    :raise: BadPermutationError or ValueError
    """
    if len(sequence) != len(permutation):
        raise ValueError((sequence, permutation))
    if not check_permutation(permutation):
        raise BadPermutationError(str(permutation))
    
    if type(sequence) in (list, tuple, str):
        constructor = type(sequence)
    else:
        constructor = list
    return constructor((sequence[p] for p in permutation))

def full_block_perm(block_permutation, block_structure):
    """
    Extend a permutation of blocks to a permutation for the internal signals of all blocks.
    E.g., say we have two blocks of sizes ('block structure') ``(2, 3)``,
    then a block permutation that switches the blocks would be given by the image tuple ``(1,0)``.
    However, to get a permutation of all 2+3 = 5 channels that realizes that block permutation we would need
    ``(2, 3, 4, 0, 1)``

    :param block_permutation: permutation image tuple of block indices
    :type block_permutation: tuple
    :param block_structure: The block channel dimensions, block structure
    :type block_structure: tuple
    :return: A single permutation for all channels of all blocks.
    :rtype: tuple
    """
    fblockp = []
    bp_inv = invert_permutation(block_permutation)
    for k, block_length in enumerate(block_structure):
        p_k = block_permutation[k]
        offset = sum([block_structure[bp_inv[j]] for j in range(p_k)])
        fblockp += range(offset, offset + block_length)

    assert sorted(fblockp) == range(sum(block_structure))

    return tuple(fblockp)

def block_perm_and_perms_within_blocks(permutation, block_structure):
    """
    Decompose a permutation into a block permutation and into permutations acting within each block.

    :param permutation: The overall permutation to be factored.
    :type permutation: tuple
    :param block_structure: The channel dimensions of the blocks
    :type block_structure: tuple
    :return: ``(block_permutation, permutations_within_blocks)``
     Where ``block_permutations`` is an image tuple for a permutation of the block indices
     and ``permutations_within_blocks`` is a list of image tuples for the permutations of the channels
     within each block
    :rtype: tuple
    """
    nblocks = len(block_structure)
    cdim = sum(block_structure)

    offsets = [sum(block_structure[:k]) for k in range(nblocks)]
    images = [permutation[offset: offset + length] for (offset, length) in zip(offsets, block_structure)]

    images_mins = map(min, images)


    key_block_perm_inv = lambda block_index: images_mins[block_index]

    block_perm_inv = tuple(sorted(range(nblocks), key = key_block_perm_inv))
    # print images_mins
    # print permutation, block_structure, "-->", block_perm, invert_permutation(block_perm)
    block_perm = invert_permutation(block_perm_inv)

    assert images_mins[block_perm_inv[0]] == min(images_mins)
    assert images_mins[block_perm_inv[-1]] == max(images_mins)

    # block_perm = tuple(invert_permutation(block_perm_inv))

    perms_within_blocks = []
    for (offset, length, image) in zip(offsets, block_structure, images):
        block_key = lambda elt_index: image[elt_index]
        within_inv = sorted(range(length), key = block_key)
        within = invert_permutation(tuple(within_inv))
        assert permutation[within_inv[0] + offset] == min(image)
        assert permutation[within_inv[-1] + offset] == max(image)
        perms_within_blocks.append(within)

    return block_perm, perms_within_blocks


## TODO Add test code