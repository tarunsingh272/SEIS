# lab_8_3.py

# use this function to generate an almost-sorted list of length N,
#   containing ints 1..N

import random
from timeit import Timer
from bubble import bubble_sort
from short_bubble import bubble_sort_short
from selection import selection_sort
from insertion import insertion_sort

def almost_sorted(n):
    lst = [k for k in range(n)]
    # swap two random locations <= 10 times
    for k in range(random.randint(1,5)):
        l1 = random.randrange(n)
        l2 = random.randrange(n)
        lst[l1],lst[l2] = lst[l2],lst[l1]
    return lst

# add your code from previous Exercise below, then modify to use almost_sorted(lst)

from bubble import bubble_sort
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

calls = 10
for n in range(100,2100,100):

    t1 = Timer("bubble(lst)","from __main__ import bubble, lst")

    # lst = [random.randint(1, n) for k in range(n)]  # random array of length n
    lst = almost_sorted(n)


    # print both time and time/n*n
    time_per_sort = t1.timeit(calls)/calls
    print(f'avg time, avg/n*n for {calls} calls: {time_per_sort}, {time_per_sort/(n*n)} -> {n}')

    lst = almost_sorted(n)
    t2 = Timer("bubble2(lst)", "from __main__ import bubble2, lst")

    # print both time and time/n*n
    time_per_sort = t2.timeit(calls) / calls
    print(f'(2) avg time, avg/n*n for {calls} calls: {time_per_sort}, {time_per_sort / (n * n)} -> {n}')

    lst = almost_sorted(n)
    t3 = Timer("selection(lst)", "from __main__ import selection, lst")
    # print both time and time/n*n
    time_per_sort = t3.timeit(calls) / calls
    print(f'(3) avg time, avg/n*n for {calls} calls: {time_per_sort}, {time_per_sort / (n * n)} -> {n}')

    lst = almost_sorted(n)
    t4 = Timer("insertion(lst)", "from __main__ import insertion, lst")
    # print both time and time/n*n
    time_per_sort = t4.timeit(calls) / calls
    print(f'(4) avg time, avg/n*n for {calls} calls: {time_per_sort}, {time_per_sort / (n * n)} -> {n}')
