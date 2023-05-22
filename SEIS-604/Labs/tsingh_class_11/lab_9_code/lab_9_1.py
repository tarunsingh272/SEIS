# lab_9_1.py

# Radix Sort!

from queue47 import Queue # avoid queue.py, which interferes...import

import random

num_digits = 10 # how many digits?
q = Queue() # main queue

for count in range(100):
    q.enqueue(random.randint(1,100))

qlist = [Queue() for k in range(num_digits)] # qlist[i] is queue for digit i

# let's see what we might do...

length_of_longest = 4
for i in range(length_of_longest): # ith digit from rightmost
    # sort q into digit bins
    while not q.is_empty():
        pass
        # get the next element e from the queue
        e = q.dequeue()
        # calc its bin_number by (e//10**i) % 10
        bin_number = (e//10**i) % 10
        # enqueue it into bin_number
        qlist[bin_number].enqueue(e)

    # merge back into main bin q, smallest digit first
    # note this results in the first element of the queue being the largest,
    #

    for digit in range(0,10):
        while not qlist[digit].is_empty():
            e = qlist[digit].dequeue()
            q.enqueue(e)
        # while queue[digit] isn't empty:
        #   dequeue its elements and enqueue back into q

print (q) # should be sorted!