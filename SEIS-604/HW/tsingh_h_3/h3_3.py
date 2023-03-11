# h3_3.py

import random
import math
from timeit import Timer

def test1(lst):
     lst.sort()  # sort the lst

for mult in range(1,11):
    n = mult * 100
    lst = [random.randrange(n) for i in range(n)]
    t1 = Timer("test1(lst)", "from __main__ import test1, lst")

    # complete this by printing the time/e (t1.timeit(number=1000)/e)
    print("n==", n, "time==", t1.timeit(number=1000) / (n*math.log(n)))

