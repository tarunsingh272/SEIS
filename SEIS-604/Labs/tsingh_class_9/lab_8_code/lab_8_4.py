# lab_8_4.py

# compare timing of sequential vs binary search

from binary_search_iter import binary_search
from seq_search import seq_search

import random
import math
from timeit import Timer

# note the following repeat factor 'calls'
calls = 10
for n in range(100,2100,100):

    t1 = Timer("binary_search(lst,item)","from __main__ import binary_search, lst, item")

    lst = [random.randint(1, n) for k in range(n)]  # random array of length n
    item = random.randint(1,n)

    # print both time and time/log(n)
    time_per_search = t1.timeit(calls)/calls
    print(f'(BS) avg time, avg/n*n for {calls} calls: {time_per_search}, {time_per_search/(math.log(n))} -> {n}')

    t2 = Timer("binary_search(lst,item)", "from __main__ import seq_search, lst, item")

    lst = [random.randint(1, n) for k in range(n)]  # random array of length n
    item = random.randint(1, n)

    # print both time and time/log(n)
    time_per_search = t2.timeit(calls) / calls
    print(f'(SS) avg time, avg/n*n for {calls} calls: {time_per_search}, {time_per_search / n)} -> {n}')

