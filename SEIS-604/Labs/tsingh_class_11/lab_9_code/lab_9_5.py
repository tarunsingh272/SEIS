# lab_9_5.py

# timing experiment for heap sort vs mergesort and quicksort

# import heap_sort from lab_9_4.py and merge_sort from merge.py

import random
import math
from timeit import Timer
from merge import merge_sort
from lab_9_4 import heap_sort

# note the following repeat factor 'calls'
calls = 10
for n in range(100,2100,100):
    lst = [random.randint(1, n) for k in range(n)]  # random array of length n
    lst2 = lst[:] # clone it

    t1 = Timer("heap_sort(lst)","from __main__ import heap_sort, lst")

    # print both time and time/(n*log(n))
    time_per_search = t1.timeit(calls)/calls
    print(f'(HeapSort) avg time, avg/(n*log(n)) for {calls} calls: {time_per_search}, {time_per_search/(n*math.log(n))} -> {n}')

    t2 = Timer("merge_sort(lst2)","from __main__ import merge_sort, lst2")

    # print both time and time/log(n)
    time_per_search = t2.timeit(calls)/calls
    print(f'(MergeSort) avg time, avg/(n*log(n))) for {calls} calls: {time_per_search}, {time_per_search/(n*math.log(n))} -> {n}')

 #  do the same kind of timing for as many sorting methods as you can


def main():
    ''' finish this'''

main()


