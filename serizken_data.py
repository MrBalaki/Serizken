from itertools import permutations
from serizken import satisfy_placement_condition, terminal_pawns, gen_edges

nodes = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 6))
nodes = list(filter(satisfy_placement_condition, nodes))

lt = {t for t in nodes if t[:3] in terminal_pawns}
rt = {t for t in nodes if t[3:] in terminal_pawns}

G_lf = {node:gen_edges(node, True) for node in nodes}
G_rf = {node:gen_edges(node, False) for node in nodes}
