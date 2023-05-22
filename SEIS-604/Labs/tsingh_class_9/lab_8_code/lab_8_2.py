# lab_8_2.py

import random
from timeit import Timer
from bubble import bubble_sort
from short_bubble import bubble_sort_short
from selection import selection_sort
from insertion import insertion_sort

def bubble(lst):
    bubble_sort(lst)

def bubble2(lst):
    bubble_sort_short(lst)

def selection(lst):
    selection_sort(lst)

def insertion(lst):
    insertion_sort(lst)

# wrap the above tests in a loop that divides the timings for n==100..1000 by 100's
#  by O(f(n)), where f(n) is your guess as to the performance

# note the following repeat factor 'calls'
calls = 10
for n in range(100,2100,100):

    t1 = Timer("bubble(lst)","from __main__ import bubble, lst")

    lst = [random.randint(1, n) for k in range(n)]  # random array of length n

    # print both time and time/n*n
    time_per_sort = t1.timeit(calls)/calls
    print(f'avg time, avg/n*n for {calls} calls: {time_per_sort}, {time_per_sort/(n*n)} -> {n}')

    t2 = Timer("bubble2(lst)", "from __main__ import bubble2, lst")

    lst = [random.randint(1, n) for k in range(n)]  # random array of length n

    # print both time and time/n*n
    time_per_sort = t2.timeit(calls) / calls
    print(f'(2) avg time, avg/n*n for {calls} calls: {time_per_sort}, {time_per_sort / (n * n)} -> {n}')

    t3 = Timer("selection(lst)", "from __main__ import selection, lst")
    # print both time and time/n*n
    time_per_sort = t3.timeit(calls) / calls
    print(f'(3) avg time, avg/n*n for {calls} calls: {time_per_sort}, {time_per_sort / (n * n)} -> {n}')

    t4 = Timer("insertion(lst)", "from __main__ import insertion, lst")
    # print both time and time/n*n
    time_per_sort = t4.timeit(calls) / calls
    print(f'(4) avg time, avg/n*n for {calls} calls: {time_per_sort}, {time_per_sort / (n * n)} -> {n}')