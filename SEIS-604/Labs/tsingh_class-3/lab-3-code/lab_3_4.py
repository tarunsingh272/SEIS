# lab_3_4.py

# replace indexing by concatenating the list with itself...

import random
from timeit import Timer

def test1(lst,i):
    fetched = lst[i] # index into lst for timing

def test2(lst):
    result = lst + lst # concatenate lst with itself

def test3(lst):
    lst.pop()

def test4(lst):
    lst.pop(0)

for mult in range(1,11):
    n = mult * 1000
    lst = [k for k in range(n)] # build a list of length n

    i = random.randint(0, len(lst) - 1) # pick a random index
    t2 = Timer("test3(lst)", "from __main__ import test3, lst")
    e = n # replace with correct e for O(e) as performance of self-concatenating list of length n
    print ("n==", n, "time==", t2.timeit(number=1000) / n)

