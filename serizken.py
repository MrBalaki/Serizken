trans = {
    1 : [2, 4],
    2 : [1, 3, 5],
    3 : [2, 6],
    4 : [1, 5, 7],
    5 : [2, 4, 6, 8],
    6 : [3, 5, 9],
    7 : [4, 8],
    8 : [5, 7, 9],
    9 : [6, 8]
    }

terminal_pawns = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (1, 4, 7),
    (2, 5, 8),
    (3, 6, 9),
    (1, 5, 9),
    (3, 5, 7)
    ]

def gen_edges(node, left_move):
    node = list(node)
    left_pawns = node[:3]
    right_pawns = node[3:]

    edges = []

    if left_move:
        for i in range(3):
            p = left_pawns[i]
            for m in [m for m in trans[p] if m not in node]:
                left_pawns[i] = m
                perm = part_sorted(left_pawns+right_pawns)
                if perm not in edges:
                    edges.append(perm)
            left_pawns[i] = p # Restore
    else:
        for i in range(3):
            p = right_pawns[i]
            for m in [m for m in trans[p] if m not in node]:
                right_pawns[i] = m
                perm = part_sorted(left_pawns+right_pawns)
                if perm not in edges:
                    edges.append(perm)
            right_pawns[i] = p # Restore
    
    return edges

def replace_at(source, index, value):
    return source[0:index]+type(source)((value,))+source[index+1:]

def satisfy_placement_condition(node):
    return (node[0] < node[1] and node[1] < node[2]) and (node[3] < node[4] and node[4] < node[5])

def part_sorted(tple : tuple):
    l = list(tple[:3])
    l.sort()
    r = list(tple[3:])
    r.sort()

    return tuple(l + r)

def distances_to_node(adj_graph : dict, node : tuple):
    queue = [node]
    visited = {node}
    distances = {}

    for n in adj_graph.keys():
        distances[n] = float('inf')
    distances[node] = 0

    while queue:
        n = queue.pop(0)

        for m in adj_graph[n]:
            if not m in visited:
                distances[m] = distances[n]+1
                visited.add(m)
                queue.append(m)
    
    return distances