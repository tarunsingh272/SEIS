# h8_4.py

# copied from Lab 9-5

import random
import math
from timeit import Timer
from queue47 import Queue

# Radix Sort!
def radix_sort(lst):
    num_digits = 10
    q = Queue()
    for item in lst:
        q.enqueue(item)

    qlist = [Queue() for k in range(num_digits)]

    length_of_longest = 5
    for i in range(length_of_longest): # ith digit from rightmost
        # sort q into digit bins
        while not q.is_empty():
            pass
            # get the next element e from the queue
            e = q.dequeue()
            # calc its bin_number by (e//10**i) % 10
            bin_number = (e//10**i) % 10
            # enqueue it into bin_number
            qlist[bin_number].enqueue(e)

        # merge back into main bin q, smallest digit first
        # note this results in the first element of the queue being the largest,

        for digit in range(0,10):
            while not qlist[digit].is_empty():
                e = qlist[digit].dequeue()
                q.enqueue(e)
            # while queue[digit] isn't empty:
            # dequeue its elements and enqueue back into q
    return q

class BinaryHeap:
    def __init__(self):
        self._heap = []

    def _perc_up(self, cur_idx):
        while (cur_idx - 1) // 2 >= 0:
            parent_idx = (cur_idx - 1) // 2
            if self._heap[cur_idx] < self._heap[parent_idx]:
                self._heap[cur_idx], self._heap[parent_idx] = (
                    self._heap[parent_idx],
                    self._heap[cur_idx],
                )
            cur_idx = parent_idx

    def _perc_down(self, cur_idx):
        while 2 * cur_idx + 1 < len(self._heap):
            min_child_idx = self._get_min_child(cur_idx)
            if self._heap[cur_idx] > self._heap[min_child_idx]:
                self._heap[cur_idx], self._heap[min_child_idx] = (
                    self._heap[min_child_idx],
                    self._heap[cur_idx],
                )
            else:
                return
            cur_idx = min_child_idx

    def _get_min_child(self, parent_idx):
        if 2 * parent_idx + 2 > len(self._heap) - 1:
            return 2 * parent_idx + 1
        if self._heap[2 * parent_idx + 1] < self._heap[2 * parent_idx + 2]:
            return 2 * parent_idx + 1
        return 2 * parent_idx + 2

    def heapify(self, not_a_heap):
        self._heap = not_a_heap[:]
        cur_idx = len(self._heap) // 2 - 1
        while cur_idx >= 0:
            self._perc_down(cur_idx)
            cur_idx = cur_idx - 1

    def get_min(self):
        return self._heap[0]

    def insert(self, item):
        self._heap.append(item)
        self._perc_up(len(self._heap) - 1)

    def delete(self):
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        result = self._heap.pop()
        self._perc_down(0)
        return result

    def is_empty(self):
        return not bool(self._heap)

    def __len__(self):
        return len(self._heap)

    def __str__(self):
        return str(self._heap)

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


''' finish this'''
calls = 10
for n in range(100, 2100, 100):
    lst = [random.randint(1, n) for k in range(n)]  # random array of length n
    lst2 = lst[:]  # clone it

    t1 = Timer("heap_sort(lst)", "from __main__ import heap_sort, lst")

    # print both time and time/(n*log(n))
    time_per_search = t1.timeit(calls) / calls
    print(
        f'(HS) avg time, avg/(n*log(n)) for {calls} calls: {time_per_search}, {time_per_search / (n * math.log(n))} -> {n}')

    t2 = Timer("radix_sort(lst)", "from __main__ import radix_sort, lst")

    # print both time and time/log(n)
    time_per_search = t2.timeit(calls) / calls
    print(
        f'(RS) avg time, avg/(n) for {calls} calls: {time_per_search}, {time_per_search / n } -> {n}')

#Hi Prof, I was not able to call lst in main function, therefore removing main() function everything runs when we run it.
# It would be great if you can show us how to use lst when lst is defined in the main function