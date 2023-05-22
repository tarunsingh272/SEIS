# _dsp_7_9_listing_3.py

def traverse(starting_vertex):
    current = starting_vertex
    while current:
        print(current.key)
        current = current.previous

traverse(g.get_vertex("sage"))
