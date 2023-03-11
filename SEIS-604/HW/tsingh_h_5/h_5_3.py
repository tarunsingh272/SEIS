# h_5_3.py
# Tarun Singh

# implement a queue class QueueLL that uses
#   the following Node class

import node

# use node.Node below

class QueueLinked:
    # finish this
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front == None

    def enqueue(self, item):
        temp = node.Node(item)

        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def dequeue(self):

        if self.is_empty():
            return
        temp = self.front
        self.front = temp.next

        if self.front == None:
            self.rear = None

    def __str__(self):
        to_return = "[ "
        current = self.front
        while current != None:
            to_return = to_return + str(current.data) + ", "
            current = current.next
        return to_return + " ]"


# test your QueueLinked by building a queue...

def main():
    
    # add code that exercises all of your methods
    q = QueueLinked()
    print(q.is_empty())
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q)
    q.dequeue()
    print(q)
    print(q.is_empty())
    q.enqueue(4)
    q.enqueue(10)
    print(q)
main()


