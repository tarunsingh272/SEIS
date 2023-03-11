# h3-4.py - Extra Credit
# Tarun Singh

import random
import math
from timeit import Timer

# copy the five code fragments from h3-1.py and put each into
# its own function, passing the value of n

# here's the first such function:

def frag_1(n):
    count_1 = 0
    for i in range(n):
        for j in range(n):
            k = 2 + 2
            count_1 += 1  # one more asg

def frag_2(n):
    count_2 = 0
    for i in range(n):
        k = 2 + 2
        count_2 += 1

def frag_3(n):
    count_3 = 0
    i = n
    while i > 0:
        k = 2 + 2
        count_3 += 1
        i = i // 2

def frag_4(n):
    count_4 = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                k = 2 + 2
                count_4 += 1

def frag_5(n):
    count_5 = 0
    for i in range(n):
        count_5 += 1
        k = 2 + 2
    for j in range(n):
        k = 2 + 2
        count_5 += 1
    for k in range(n):
        k = 2 + 2
        count_5 += 1

#
# for each fragment, add timing code, run it, and print
#   the elapsed_time/e for where O(e) is the complexity of code

# fragment 1 is done for you...

for mult in range(1,11):
    n = mult * 100
    # timing fragment 1:
    t1 = Timer("frag_1(n)","from __main__ import frag_1, n")
    time_t1 = t1.timeit(1000)
    print ("n=",n, "ratio is:", time_t1/n**2) # O(n**2)

    # timing fragment 2:
    t2 = Timer("frag_2(n)", "from __main__ import frag_2, n")
    time_t2 = t2.timeit(1000)
    print("n=", n, "ratio is:", time_t2 / n)  # O(n)

    # timing fragment 3:
    t3 = Timer("frag_3(n)", "from __main__ import frag_3, n")
    time_t3 = t3.timeit(1000)
    print("n=", n, "ratio is:", time_t3 / math.log(n))  # O(log(n))

    # timing fragment 4:
    t4 = Timer("frag_4(n)", "from __main__ import frag_4, n")
    time_t4 = t4.timeit(1000)
    print("n=", n, "ratio is:", time_t4 / n ** 3)  # O(n**3)

    # timing fragment 5:
    t5 = Timer("frag_5(n)", "from __main__ import frag_5, n")
    time_t5 = t5.timeit(1000)
    print("n=", n, "ratio is:", time_t5 / n)  # O(n)

    # finish with other fragments

