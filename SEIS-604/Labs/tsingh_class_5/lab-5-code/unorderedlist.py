# part of Lab 5 Exercises 2 & 3

import node

class UnorderedList:
    def __init__(self):
        self.head = None
        self.tail = None # points to last node

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = node.Node(item)
        temp.set_next(self.head)
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

    def __str__(self):
        to_return = "["
        current = self.head
        while current != None:
            to_return = to_return + str(current.data) + ","
            current = current.next
        return to_return + "]"

    def append(self, item):

        if self.head == None:
            temp = node.Node(item)
            self.head = temp
            self.tail = temp
        else:
            temp = node.Node(item)
            self.tail.next = temp
            self.tail = temp

"""        current = self.head
        previous = None

        while current != None:
            previous = current
            current = current.next

        if self.head == None:  # appending to empty list
            self.head = temp
            temp.next = None
        else:
            previous.next = temp
            temp.next = None
"""

my_list = UnorderedList()
my_list.append(47)
print(my_list)
my_list.append(23)
print(my_list)
my_list.add("moxie")
print(my_list)

def main():
    my_list = UnorderedList()

    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)

    print(my_list.size())
    print(my_list.search(93))
    print(my_list.search(100))

    my_list.add(100)
    print(my_list.search(100))
    print(my_list.size())

    my_list.remove(54)
    print(my_list.size())
    my_list.remove(93)
    print(my_list.size())
    my_list.remove(31)
    print(my_list.size())
    print(my_list.search(93))

    try:
        my_list.remove(27)
    except ValueError as ve:
        print(ve)
# main()