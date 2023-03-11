#
# orderedlist.py: part of h_5 and imported by some of them
#

# part of h_5

class Node:
    """A node of a linked list"""

    def __init__(self, node_data):
        self._data = node_data
        self._next = None

    def get_data(self):
        """Get node data"""
        return self._data

    def set_data(self, node_data):
        """Set node data"""
        self._data = node_data

    data = property(get_data, set_data)

    def get_next(self):
        """Get next node"""
        return self._next

    def set_next(self, node_next):
        """Set next node"""
        self._next = node_next

    next = property(get_next, set_next)

    def __str__(self):
        """String"""
        return str(self._data)

class OrderedList:
    """Ordered linked list implementation"""
    def __init__(self):
        self.head = None

    def search(self, item):
        """Search for a node with a specific value"""
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            if current.data > item:
                return False
            current = current.next

        return False

    def add(self, item):
        """Add a new node"""
        current = self.head
        previous = None
        temp = Node(item)

        while current is not None and current.data < item:
            previous = current
            current = current.next

        if previous is None:
            temp.next = self.head
            self.head = temp
        else:
            temp.next = current
            previous.next = temp

    def is_empty(self):
        """Is the list empty"""
        return self.head == None

    def size(self):
        """Size of the list"""
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next

        return count

    def __str__(self):
        to_return = "["
        current = self.head
        while current != None:
            to_return = to_return + str(current.data) + ","
            current = current.next
        return to_return + "]"

