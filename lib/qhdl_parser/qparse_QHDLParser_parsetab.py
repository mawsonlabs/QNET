
# /Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse_QHDLParser_parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\xa5\xdcT\xd4\xd0:t.\xe2qP=\xca\xa2Y\xf6'
    
_lr_action_items = {'REAL':([43,],[59,]),'FEEDLEFT':([83,101,],[102,102,]),'GENERIC':([10,44,103,],[13,13,111,]),'ENTITY':([0,1,3,5,6,9,23,69,125,],[2,-3,-4,-2,2,-1,34,-5,-42,]),'COMPLEX':([43,],[62,]),'PORT':([10,12,14,15,44,63,75,103,112,113,137,],[-14,19,-12,-13,-14,19,-15,-14,121,-56,-55,]),'BEGIN':([30,46,47,67,114,],[45,-50,-43,-49,-51,]),'RPAREN':([25,26,37,38,39,40,41,54,55,56,59,60,61,62,73,76,78,87,88,90,91,92,93,94,96,97,123,128,129,130,131,136,138,139,],[-14,-17,-14,-37,-10,57,-11,-10,74,-16,-21,-23,-14,-22,-36,-18,-25,-38,-41,-29,-31,-28,-24,-27,-26,-30,128,-32,133,-58,-60,140,-57,-59,]),'FCONST':([77,95,115,],[91,91,91,]),'SEMI':([23,25,26,33,34,35,37,38,50,51,52,56,57,59,60,61,62,73,74,76,78,87,88,90,91,92,93,94,96,97,99,104,106,107,108,109,110,116,117,128,133,140,],[-14,39,-17,-14,-6,-7,54,-37,69,-8,-9,-16,75,-21,-23,-14,-22,-36,89,-18,-25,-38,-41,-29,-31,-28,-24,-27,-26,-30,-14,114,-14,-44,-14,-45,118,124,125,-32,137,141,]),'COLON':([27,28,36,58,66,68,83,],[43,-20,53,-19,85,86,85,]),'COMMA':([27,28,36,58,68,90,91,92,97,105,129,130,131,136,138,139,],[42,-20,42,-19,42,-29,-31,-28,-30,115,134,-58,-60,134,-57,-59,]),'ASSIGN':([59,60,61,62,],[-21,-23,77,-22,]),'OUT':([53,],[72,]),'END':([10,12,14,15,17,18,20,44,63,64,65,75,79,80,81,82,84,89,100,103,112,113,118,120,122,137,141,],[-14,-14,-12,-13,23,-33,-34,-14,-14,-14,-53,-15,98,99,-64,-52,-66,-35,-63,-14,-14,-56,-65,-54,-62,-55,-61,]),'IS':([7,16,],[10,22,]),'FEEDRIGHT':([131,],[135,]),'ICONST':([77,95,115,],[97,97,97,]),'LPAREN':([13,19,77,119,127,],[21,24,95,126,132,]),'IN':([53,],[71,]),'ID':([2,4,11,21,23,24,29,33,34,35,39,42,45,48,54,64,65,80,81,82,84,85,99,100,102,103,106,107,108,109,112,113,118,120,122,126,132,134,135,137,141,],[7,8,16,28,-14,28,44,51,-6,-7,28,58,66,28,28,83,-53,101,-64,-52,-66,103,-14,-63,110,-14,51,-44,51,-45,-14,-56,-65,-54,-62,131,131,131,139,-55,-61,]),'MAP':([111,121,],[119,127,]),'INT':([43,],[60,]),'OF':([8,],[11,]),'SIGNAL':([31,32,46,47,49,67,114,124,],[-47,48,-50,48,-46,-49,-51,-48,]),'COMPONENT':([22,31,32,49,98,124,],[29,-47,29,-46,106,-48,]),'ARCHITECTURE':([0,1,3,5,6,9,69,99,125,],[4,-3,-4,-2,4,-1,-5,107,-42,]),'$end':([1,3,5,6,9,69,125,],[-3,-4,-2,0,-1,-5,-42,]),'FIELDMODE':([70,71,72,86,],[88,-39,-40,88,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'instance_mapping_assignment_list':([45,],[64,]),'signal_list':([32,],[47,]),'int':([77,95,115,],[92,92,92,]),'feedright_assignment_list':([126,132,],[129,136,]),'entity_declaration':([0,6,],[1,1,]),'opt_semi':([25,37,],[40,55,]),'port_statement':([12,63,],[18,18,]),'generic_type':([43,],[61,]),'id_list':([21,24,39,48,54,],[27,36,27,68,36,]),'signal_direction':([53,],[70,]),'number':([77,],[93,]),'generic_clause':([10,44,],[12,63,]),'architecture_head':([22,],[30,]),'architecture_declaration':([0,6,],[3,3,]),'complex':([77,],[94,]),'generic_statement':([10,44,],[14,14,]),'component_declaration_list':([22,],[32,]),'generic_default':([61,],[76,]),'simple_number':([77,95,115,],[96,105,123,]),'empty':([10,12,23,25,33,37,44,61,63,64,80,99,103,106,108,112,],[15,20,35,41,52,41,15,78,20,84,84,109,113,52,52,122,]),'real':([77,95,115,],[90,90,90,]),'opt_entity':([23,],[33,]),'feedleft_assignment':([64,80,],[81,100,]),'opt_arch':([99,],[108,]),'port_map':([112,],[120,]),'generic_entry_group':([21,39,],[26,56,]),'feedright_assignment':([126,132,134,],[130,130,138,]),'opt_id':([33,106,108,],[50,116,117,]),'port_list':([24,],[37,]),'instance_mapping_assignment':([45,64,],[65,82,]),'component_declaration':([22,32,],[31,49,]),'top_level_list':([0,],[6,]),'port_entry_group':([24,54,],[38,73,]),'port_clause':([12,63,],[17,79,]),'signal_entry_group':([32,47,],[46,67,]),'generic_list':([21,],[25,]),'generic_map':([103,],[112,]),'feedleft_assignment_list':([64,],[80,]),'signal_type':([70,86,],[87,104,]),'top_level_unit':([0,6,],[5,9,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> top_level_list","S'",1,None,None,None),
  ('top_level_list -> top_level_list top_level_unit','top_level_list',2,'p_top_level_list','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',155),
  ('top_level_list -> top_level_unit','top_level_list',1,'p_top_level_list','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',156),
  ('top_level_unit -> entity_declaration','top_level_unit',1,'p_top_level_unit','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',183),
  ('top_level_unit -> architecture_declaration','top_level_unit',1,'p_top_level_unit','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',184),
  ('entity_declaration -> ENTITY ID IS generic_clause port_clause END opt_entity opt_id SEMI','entity_declaration',9,'p_entity_declaration','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',190),
  ('opt_entity -> ENTITY','opt_entity',1,'p_opt_entity','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',203),
  ('opt_entity -> empty','opt_entity',1,'p_opt_entity','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',204),
  ('opt_id -> ID','opt_id',1,'p_opt_id','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',210),
  ('opt_id -> empty','opt_id',1,'p_opt_id','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',211),
  ('opt_semi -> SEMI','opt_semi',1,'p_opt_semi','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',217),
  ('opt_semi -> empty','opt_semi',1,'p_opt_semi','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',218),
  ('generic_clause -> generic_statement','generic_clause',1,'p_generic_clause','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',224),
  ('generic_clause -> empty','generic_clause',1,'p_generic_clause','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',225),
  ('empty -> <empty>','empty',0,'p_empty','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',233),
  ('generic_statement -> GENERIC LPAREN generic_list opt_semi RPAREN SEMI','generic_statement',6,'p_generic_statement','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',240),
  ('generic_list -> generic_list SEMI generic_entry_group','generic_list',3,'p_generic_list','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',246),
  ('generic_list -> generic_entry_group','generic_list',1,'p_generic_list','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',247),
  ('generic_entry_group -> id_list COLON generic_type generic_default','generic_entry_group',4,'p_generic_entry_group','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',256),
  ('id_list -> id_list COMMA ID','id_list',3,'p_id_list','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',263),
  ('id_list -> ID','id_list',1,'p_id_list','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',264),
  ('generic_type -> REAL','generic_type',1,'p_generic_type','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',273),
  ('generic_type -> COMPLEX','generic_type',1,'p_generic_type','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',274),
  ('generic_type -> INT','generic_type',1,'p_generic_type','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',275),
  ('generic_default -> ASSIGN number','generic_default',2,'p_generic_default','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',280),
  ('generic_default -> empty','generic_default',1,'p_generic_default','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',281),
  ('number -> simple_number','number',1,'p_number','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',290),
  ('number -> complex','number',1,'p_number','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',291),
  ('simple_number -> int','simple_number',1,'p_simple_number','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',297),
  ('simple_number -> real','simple_number',1,'p_simple_number','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',298),
  ('int -> ICONST','int',1,'p_int','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',304),
  ('real -> FCONST','real',1,'p_real','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',310),
  ('complex -> LPAREN simple_number COMMA simple_number RPAREN','complex',5,'p_complex','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',317),
  ('port_clause -> port_statement','port_clause',1,'p_port_clause','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',323),
  ('port_clause -> empty','port_clause',1,'p_port_clause','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',324),
  ('port_statement -> PORT LPAREN port_list opt_semi RPAREN SEMI','port_statement',6,'p_port_statement','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',334),
  ('port_list -> port_list SEMI port_entry_group','port_list',3,'p_port_list','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',340),
  ('port_list -> port_entry_group','port_list',1,'p_port_list','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',341),
  ('port_entry_group -> id_list COLON signal_direction signal_type','port_entry_group',4,'p_port_entry_group','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',350),
  ('signal_direction -> IN','signal_direction',1,'p_signal_direction','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',356),
  ('signal_direction -> OUT','signal_direction',1,'p_signal_direction','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',357),
  ('signal_type -> FIELDMODE','signal_type',1,'p_signal_type','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',363),
  ('architecture_declaration -> ARCHITECTURE ID OF ID IS architecture_head BEGIN instance_mapping_assignment_list feedleft_assignment_list END opt_arch opt_id SEMI','architecture_declaration',13,'p_architecture_declaration','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',369),
  ('architecture_head -> component_declaration_list signal_list','architecture_head',2,'p_architecture_head','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',385),
  ('opt_arch -> ARCHITECTURE','opt_arch',1,'p_opt_arch','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',391),
  ('opt_arch -> empty','opt_arch',1,'p_opt_arch','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',392),
  ('component_declaration_list -> component_declaration_list component_declaration','component_declaration_list',2,'p_component_declaration_list','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',399),
  ('component_declaration_list -> component_declaration','component_declaration_list',1,'p_component_declaration_list','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',400),
  ('component_declaration -> COMPONENT ID generic_clause port_clause END COMPONENT opt_id SEMI','component_declaration',8,'p_component_declaration','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',410),
  ('signal_list -> signal_list signal_entry_group','signal_list',2,'p_signal_list','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',419),
  ('signal_list -> signal_entry_group','signal_list',1,'p_signal_list','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',420),
  ('signal_entry_group -> SIGNAL id_list COLON signal_type SEMI','signal_entry_group',5,'p_signal_entry_group','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',430),
  ('instance_mapping_assignment_list -> instance_mapping_assignment_list instance_mapping_assignment','instance_mapping_assignment_list',2,'p_instance_mapping_assignment_list','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',439),
  ('instance_mapping_assignment_list -> instance_mapping_assignment','instance_mapping_assignment_list',1,'p_instance_mapping_assignment_list','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',440),
  ('instance_mapping_assignment -> ID COLON ID generic_map port_map','instance_mapping_assignment',5,'p_instance_mapping_assignment','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',449),
  ('generic_map -> GENERIC MAP LPAREN feedright_assignment_list RPAREN SEMI','generic_map',6,'p_generic_map','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',455),
  ('generic_map -> empty','generic_map',1,'p_generic_map','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',456),
  ('feedright_assignment_list -> feedright_assignment_list COMMA feedright_assignment','feedright_assignment_list',3,'p_feedright_assignment_list','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',465),
  ('feedright_assignment_list -> feedright_assignment','feedright_assignment_list',1,'p_feedright_assignment_list','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',466),
  ('feedright_assignment -> ID FEEDRIGHT ID','feedright_assignment',3,'p_feedright_assignment','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',491),
  ('feedright_assignment -> ID','feedright_assignment',1,'p_feedright_assignment','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',492),
  ('port_map -> PORT MAP LPAREN feedright_assignment_list RPAREN SEMI','port_map',6,'p_port_map','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',501),
  ('port_map -> empty','port_map',1,'p_port_map','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',502),
  ('feedleft_assignment_list -> feedleft_assignment_list feedleft_assignment','feedleft_assignment_list',2,'p_feedleft_assignment_list','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',511),
  ('feedleft_assignment_list -> feedleft_assignment','feedleft_assignment_list',1,'p_feedleft_assignment_list','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',512),
  ('feedleft_assignment -> ID FEEDLEFT ID SEMI','feedleft_assignment',4,'p_feedleft_assignment','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',525),
  ('feedleft_assignment -> empty','feedleft_assignment',1,'p_feedleft_assignment','/Users/nikolas/Projects/MabuchiLab/QNET/lib/qhdl_parser/qparse.py',526),
]
