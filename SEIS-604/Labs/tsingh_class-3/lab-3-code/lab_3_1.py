# lab_3_1.py

import math

# add code to count # of asgs made for each value of n

import math  # for math.log(N) function

for n in range(100,1100,100):

    print("processing for n==", n)

    # 1.

    count_1 = 0
    for i in range(n):
        for j in range(n):
            k = 2 + 2
            count_1 += 1  # one more asg

    # O(e) is O(n**2) for above doubly-nested loops

    # replace ??? with correct value, as well as replace 0 with count_1 / ???
    print ("1. is roughly O(n**2) with ratio:", count_1/n**2)

    # 2.

    count_2 = 0
    for i in range(n):
        k = 2 + 2
        count_2 += 1

    # O(???) is Big-O performance of above loops: # of asgs statements executed

    # replace ??? with correct value, as well as replace 0 with count_2 / ???
    print ("2. is roughly O(n) with ratio:", count_2/(n))

    # 3.

    count_3 = 0
    i = n
    while i > 0:
        k = 2 + 2
        count_3 += 1
        i = i // 2

    # O(???) is Big-O performance of above loops: # of asgs statements executed

    # replace ??? with correct value, as well as replace 0 with count_3 / ???
    print("3. is roughly O(log(n)) with ratio:",count_3/(math.log(n)))

    # 4.

    count_4 = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                k = 2 + 2
                count_4 += 1

    # O(???) is Big-O performance of above loops: # of asgs statements executed

    # replace ??? with correct value, as well as replace 0 with count_4 / ???
    print("4. is roughly O(n**3) with ratio:", count_4/n**3)

    # 5.

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

    # O(???) is Big-O performance of above loops: # of asgs statements executed

    # replace ??? with correct value, as well as replace 0 with count_5 / ???
    print ("5. is roughly O(???) with ratio:",0)

