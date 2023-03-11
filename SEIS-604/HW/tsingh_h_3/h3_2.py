# h3_2.py
# Tarun Singh

import random
from timeit import Timer

def test1(dic,i):
     fetched = dic[i]  # get item for key i in dic for timing

def test2(dic,i):
    dic[i] = 10     # set item (any) for key i in dic for timing

for mult in range(1,11):
    n = mult * 100
    dic = {k : k for k in range(n)} # build a dictionary of length n
    i = random.randint(0, len(dic) - 1) # pick a random key to look up

    t1 = Timer("test1(dic,i)", "from __main__ import test1, dic, i")

    # complete this by printing the execution time/e
    #   t1.timeit(number=1000)/e where O(e) is get item complexity

    print("n==", n, "time test1==", t1.timeit(number=1000) / 1)  # dict is O(1)

    # do the same for set item and test2(dic,i)

    dic = {k : k for k in range(n)} # build a dictionary of length n
    i = random.randint(0, len(dic) - 1) # pick a random key to look up

    t2 = Timer("test2(dic,i)", "from __main__ import test2, dic, i")

    # printing the execution time/e t2.timeit(number=1000)/e where O(e) is set item complexity

    print("n==", n, "time test2==", t2.timeit(number=1000) / 1)  # dict is O(1)
