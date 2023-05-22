# lab10_2.py

from pythonds3.graphs import Graph
from pythonds3.graphs import Vertex

def knight_graph(board_size):
    kt_graph = Graph()
    for row in range(board_size):
        for col in range(board_size):
            node_id = row * board_size + col
            new_positions = gen_legal_moves(row, col, board_size)
            for row2, col2 in new_positions:
                other_node_id = row2 * board_size + col2
                kt_graph.add_edge(node_id, other_node_id)
    return kt_graph

def gen_legal_moves(row, col, board_size):
    new_moves = []
    move_offsets = [
        (-1, -2),  # left-down-down
        (-1, 2),   # left-up-up
        (-2, -1),  # left-left-down
        (-2, 1),   # left-left-up
        (1, -2),   # right-down-down
        (1, 2),    # right-up-up
        (2, -1),   # right-right-down
        (2, 1),    # right-right-up
    ]
    for r_off, c_off in move_offsets:
        if 0 <= row + r_off < board_size and 0 <= col + c_off < board_size:
            new_moves.append((row + r_off, col + c_off))
    return new_moves

from pythonds3.graphs import Graph

def knight_tour(n, path, u, limit):
    u.color = "gray"
    path.append(u)
    if n < limit:
        neighbors = order_by_avail(u)
        i = 0
        done = False
        while i < len(neighbors) and not done:
            print (f"Exploring {u.key},{n}--{neighbors[i].get_key()}")
            # print (path)
            if neighbors[i].color == "white":
                done = knight_tour(n + 1, path, neighbors[i], limit)
            i = i + 1
        if not done:  # prepare to backtrack
            path.pop()
            u.color = "white"
    else:
        done = True
    return done

def order_by_avail(n):
    res_list = []
    for v in n.get_neighbors():
        if v.color == "white":
            c = 0
            for w in v.get_neighbors():
                if w.color == "white":
                    c = c + 1
            res_list.append((c, v))
    res_list.sort(key=lambda x: x[0])
    return [y[1] for y in res_list]

def main():
    k_graph = knight_graph(6) # 8 takes a LONG TIME to complete...
    path = []
    start_vertex = k_graph.get_vertex(47)
    print (knight_tour(0,path,start_vertex,255))
    for v in path:
        print (f"{v.key}",end='-')

    print()
main()
