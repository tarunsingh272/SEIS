# _dsp-6_10_1_heap1.py

from pythonds3.trees import BinaryHeap

my_heap = BinaryHeap()
my_heap.insert(5)
my_heap.insert(7)
my_heap.insert(3)
my_heap.insert(11)

print(my_heap.delete())
print(my_heap.delete())
print(my_heap.delete())
print(my_heap.delete())
