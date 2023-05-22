# lab_8_5.py

# Radix Sort!

from queue import Queue

N = 10 # how many digits?
q = Queue() # main queue

qlist = [Queue() for k in range(N)] # qlist[i] is queue for digit i

# let's see what we might do...
for i in range(10):

    while not q.is_empty():
        elt = q.dequeue()
        bin_number = (elt // 10 ** i) % 10
        qlist[bin_number].append(elt)



