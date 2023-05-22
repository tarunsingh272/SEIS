# lab_9_4.py

from random import randint

# implement heap sort using binary heap

from binary_heap import BinaryHeap

def heap_sort(lst2sort):
    # build a min heap hp from lst2sort

    hp = BinaryHeap()

    hp.heapify(lst2sort) # does min heap, where each parent >= either child

    # build a return a list by iterating over hp,
    #  removing the min element at the top via each time

    to_return = []
    while not hp.is_empty():
        least = hp.delete()
        to_return.append(least)

    # complete this

    return to_return

def main():
    N = 100
    to_sort = [randint(0,2*N) for i in range(N)]
    print (to_sort)

    sorted_list = heap_sort(to_sort)

    print (sorted_list)

main()
