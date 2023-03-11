# part of H 5 Exercise 2

import node

class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = node.Node(item)
        temp.set_next(self.head)
        # works, but better to do:  temp.next = self.head
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next

        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next

        return False

    def remove(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next

        if current is None:
            raise ValueError("{} is not in the list".format(item))
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    def append(self, item):
        current = self.head
        previous = None

        while current != None:
            previous = current
            current = current.next

        temp = node.Node(item)
        if self.head == None:  # appending to empty list
            self.head = temp
            temp.next = None
        else:
            previous.next = temp
            temp.next = None

    def index(self, item):
        current = self.head
        found = 0
        index = 0

        while current != None and not found:
            if current.data != item:
                index += 1
                current = current.next
            else:
                found = 1

        if found:
            return index
        else:
            return "Not Found"

    def pop(self):
        current = self.head
        previous = None

        if current == None:
            return "Empty list"

        while current.next != None:
            previous = current
            current = current.next

        previous.next = None
        return current.data

    def insert(self, pos, item):
        current = self.head
        previous = None
        index = 0
        temp = node.Node(item)

        while current != None and index < pos:
            previous = current
            current = current.next
            index += 1

        if pos == 0:
            temp.next = self.head
            self.head = temp
        else:
            if current == None:
                previous.next = temp
            else:
                temp.next = current
                previous.next = temp

    def __str__(self):
        to_return = "[ "
        current = self.head
        while current != None:
            to_return = to_return + str(current.data) + ", "
            current = current.next

        return to_return + " ]"