# lab_9_3.py

# (a) convert provided BTNode code to use the linked node approach
# (b) complete the following function that takes a root node of your BinaryTreeNode tree
#       and returns its list representation.  Hint:  recursion!

class BTNode: # TreeNode, modified for plain BT

    def __init__(self, value, left=None, right=None, parent=None):
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

    def __iter__(self):
        if self:
            if self.left_child:
                for elem in self.left_child:
                    yield elem
            yield self.value
            if self.right_child:
                for elem in self.right_child:
                    yield elem

def print_binary_tree2(root): # only works for node rep of a binary tree...
    for node in root:
        print(node)

def make_binary_tree(root_val):
    return [root_val, [], []]

def make_binary_tree2(root_val):
    '''finish this'''
    root = BTNode(root_val)
    return root

def insert_left(root, new_child):
    old_child = root.pop(1)
    if len(old_child) > 1:
        root.insert(1, [new_child, old_child, []])
    else:
        root.insert(1, [new_child, [], []])
    return root

def insert_left2(root, new_child):
    '''finish this'''
    old_child = root.left_child
    if old_child:
        new_node = BTNode(new_child, old_child, None)
        root.left_child = new_node
    else:
        root.left_child = BTNode(new_child)

    return root

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

def convert_to_list(a_tree):
    ''' build and return list, assuming a_tree is a binary tree with node implementation'''
    # base case: a_tree has no children

def main():
    ''' the following code builds a binary tree using BinaryTreeNode '''
    newtree = make_binary_tree(47)
    print (newtree)
    insert_left(newtree,29)
    print (newtree)
    insert_right(newtree[1],13)
    print (newtree)

    # add some more examples....
    # repeat the above for this tree list, building a node-based BT:

    # [9, [11, [5, [4, [], []], []], []], [7, [], [6, [], []]]]

    tree2 = make_binary_tree(9)
    node5 = BTNode(5)
    node5.left_child(BTNode(4))
    node11 = BTNode(11)
    node11.left_child = node5
    tree2.left_child = node11

    # now convert the above node-based BT to list format

    # finally iterate over the tree using for elt in tree:...

main()