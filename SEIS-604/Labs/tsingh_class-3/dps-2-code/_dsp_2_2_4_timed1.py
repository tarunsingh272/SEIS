# dsp-2_2_4_timed1.py

import time

def sum_of_n_2(n):
    start = time.time()

    the_sum = 0
    for i in range(1, n + 1):
        the_sum = the_sum + i

    end = time.time()

    return the_sum, end - start

# dsp-2_2_4_timed1.py, continued

for i in range(5):

    print("Sum is %d required %10.7f seconds" % sum_of_n_2(10000))
