# _dsp_7_22_listing_2.py

import sys
from pythonds3.trees import PriorityQueue # wrong import in book!

def prim(graph, start):
    pq = PriorityQueue()
    for vertex in graph:
        vertex.distance = sys.maxsize
        vertex.previous = None
    start.distance = 0
    pq.heapify([(vertex.distance, vertex) for vertex in graph])
    while not pq.is_empty():
        distance, current_v = pq.delete()
        for next_v in current_v.get_neighbors():
            new_distance = current_v.get_neighbor(next_v)
            if next_v in pq and new_distance < next_v.distance:
                next_v.previous = current_v
                next_v.distance = new_distance
                pq.change_priority(next_v, new_distance)
