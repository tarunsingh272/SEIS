# binary_tree.py:

#

class BTNode:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def is_left_child(self):
        return self.parent and self.parent.left_child is self

    def is_right_child(self):
        return self.parent and self.parent.right_child is self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    def has_any_child(self):
        return self.right_child or self.left_child

    def has_children(self):
        return self.right_child and self.left_child

    def replace_value(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        if self.left_child:
            self.left_child.parent = self
        if self.right_child:
            self.right_child.parent = self

    def find_min(self):
        current = self
        while current.left_child:
            current = current.left_child
        return current

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_child():
            if self.left_child:
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

    def __iter__(self):
        if self:
            if self.left_child:
                for elem in self.left_child:
                    yield elem
            yield self.key
            if self.right_child:
                for elem in self.right_child:
                    yield elem

# change the following list-based tree rep to one using BinaryTreeNode from above

def make_binary_tree(root_val):
    return [root_val, [], []]

def make_binary_tree2(root_val):
    '''finish this'''

def insert_left(root, new_child):
    old_child = root.pop(1)
    if len(old_child) > 1:
        root.insert(1, [new_child, old_child, []])
    else:
        root.insert(1, [new_child, [], []])
    return root

def insert_left2(root, new_child):
    '''finish this'''

def insert_right(root, new_child):
    old_child = root.pop(2)
    if len(old_child) > 1:
        root.insert(2, [new_child, [], old_child])
    else:
        root.insert(2, [new_child, [], []])
    return root

def insert_right2(root, new_child):
    '''finish this'''

def get_root_val(root):
    return root[0]

def get_root_val2(root):
    '''finish this'''

def set_root_val(root, new_value):
    root[0] = new_value

def set_root_val2(root, new_value):
   '''finish this'''

def get_left_child(root):
    return root[1]

def get_left_child2(root):
    '''finish this'''

def get_right_child(root):
    return root[2]

def get_right_child2(root):
    return root[2]

