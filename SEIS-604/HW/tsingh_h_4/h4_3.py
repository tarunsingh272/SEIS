# h4_3.py
# Tarun Singh

#
# Implement __str__ in Queue
#

import queue

# create two Queues, q1 and q0.
#    q1 will represent a binary 1, q0 will hold a binary 0
q1 = queue.Queue()
q0 = queue.Queue()

q1.enqueue(1)
q0.enqueue(0)

# read string bnumber with 0's and 1's only
bnumber = input("Enter the string with 0s and 1s only")

# for each
print(q1)
print(q0)