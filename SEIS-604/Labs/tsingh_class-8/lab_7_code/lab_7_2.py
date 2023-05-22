# lab 7-1:

# Implement a queue class using linked lists, including __str__().
#   The starting code includes the Node class,
#   included in node.py and imported for this problem.
#   Name your new class QueueLinked.
#   Also add code that tests your new class by creating a new QueueLinked object.
#   Then add code that adds two elements to your queue,
#   prints out the str() string of the resulting queue,
#   then removes one of the elements, printing its value.
#   Finally print the final resulting queue using str().

# The book's code is in a package pythonds3.
# The subpackage pythonds3.basic.linked_list contains
#   the LinkedListNode which is (nearly) the same as Node below

# from pythonds3.basic.linked_list import LinkedListNode as Node
from node import Node


class QueueLinked:
    def __init__(self):
        self._head = None
        self._tail = None

    def is_empty(self):
        return not bool(self._head)

    def enqueue(self, item):
        new_node = Node(item)
        if self._head == None:  # first node?
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

    def dequeue(self):
        ''' Finish this as part of Lab 6-1'''
        node_to_retun = self.head # Assume not None
        self._head = node_to_retun.next
        if self._head == None:
            self._tail = None
        return node_to_retun.data

    def size(self):
        ''' Finish this as part of Lab 6-1'''

    def __str__(self):
        ''' return queue in [e1,e2,...] format'''
        return "?"


def main():
    q = QueueLinked()
    q.enqueue(47)
    q.enqueue(29)
    print(q)


main()
