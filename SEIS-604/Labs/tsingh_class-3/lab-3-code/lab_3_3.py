# lab_3_3.py

import random
from timeit import Timer

def test1(lst,i):
     fetched = lst[i] # index into lst for timing

for mult in range(1,31):
    n = mult * 100
    lst = [k for k in range(n)] # build a list of length n

    i = random.randint(0, len(lst) - 1) # pick a random index
    
    t1 = Timer("test1(lst,i)", "from __main__ import test1, lst, i")
    print("n==", n, "time==", t1.timeit(number=1000)/n) # list[] is O(1)

