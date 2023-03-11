# lab_4_2.py

# here is the book's code on implementing the Queue ADT with the rear of the Queue
#   at the front of the list:  Queue2

# modify it so rear of Queue2 is at end of list

class Queue2:
    """alternate Queue implementation as a list"""

    def __init__(self):
        """Create new queue"""
        self._items = []

    def is_empty(self):
        """Check if the queue is empty"""
        return not bool(self._items)

    def enqueue(self, item):
        """Add an item to the queue"""
        #self._items.insert(0, item)  # end of queue at front of list
        self._items.append(item)

    def dequeue(self):
        """Remove an item from the queue"""
        # return self._items.pop() # front of queue at end of list
        return self._items.pop(0)

    def size(self):
        """Get the number of items in the queue"""
        return len(self._items)

# add code that creates a new Queue2, adds elements to it, then removes them.

q2 = Queue2()

q2.enqueue(1)
q2.enqueue(2)
q2.enqueue(3)

print(q2.dequeue())
print(q2.dequeue())
print(q2.dequeue())