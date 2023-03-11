# lab_5_5.py

# implement the StackADT as StackLink using a linked list.

# use the Node class, imported form node.py

import node

class StackLinked:
    def __init__(self):
        '''
        Creates a new stack that is empty.
        It needs no parameters and returns an empty stack.
        '''
        self.top = None


    def push(self, item):
        '''
        Adds a new item to the top of the stack.
        It needs the item and returns nothing.
        '''
        temp = node.Node(item)
        temp.next = self.top
        self.top = temp

    def pop(self):
        '''
        Removes the top item from the stack.
        It needs no parameters and returns the item.
        The stack is modified.
        '''
        if self.top == None:
            raise Exception("Cant  pop from empty stack")

        temp = self.top
        self.top = self.top.next
        return temp

    def peek(self):
        ''' returns the top item from the stack but does not remove it.
        It needs no parameters. The stack is not modified.
        '''
        pass

    def is_empty(self):
        '''
        Tests to see whether the stack is empty.
        It needs no parameters and returns a boolean value.
        '''
        if self.top == None:
            return True
        else:
            return False

    def size(self):
        '''
        Returns the number of items on the stack.
        It needs no parameters and returns an integer.
        '''


# add code to main(), creating a new StackLinked object,
#   then testing all the above methods

def main():
    pass
    # test code for StackLinked goes here...
    st = StackLinked()
    print(st.is_empty())
    st.push(47)
    print(st.is_empty())
    print(st.pop())
    print(st.is_empty())
main()