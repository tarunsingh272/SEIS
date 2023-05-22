# h8_1.py

# modify the following to implement a max heap

import random

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
            min_child_idx = self._get_max_child(cur_idx)
            if self._heap[cur_idx] < self._heap[min_child_idx]:
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

    def _get_max_child(self, parent_idx):
        if 2 * parent_idx + 2 > len(self._heap) - 1:
            return 2 * parent_idx + 1
        if self._heap[2 * parent_idx + 1] < self._heap[2 * parent_idx + 2]:
            return 2 * parent_idx + 2
        return 2 * parent_idx + 1

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

def main():
    '''
        Create a list of length 100 with random ints from 0..99,
        then 'heapify' it and repeatedly call and print delete(),
        until the tree is empty
    '''
    lst = [random.randint(1, 100) for k in range(10)]
    hp = BinaryHeap()
    hp.heapify(lst)
    to_return = []
    while not hp.is_empty():
        least = hp.delete()
        to_return.append(least)
    print(to_return)

main()