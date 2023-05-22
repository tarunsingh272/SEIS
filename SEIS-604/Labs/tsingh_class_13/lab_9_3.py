# completed implementation of a binary tree using BTNode
#
# lab_9_3.py

# (a) convert provided BTNode code to use the linked node approach
# (b) complete the following function that takes a root node of your BinaryTreeNode tree
#       and returns its list representation.  Hint:  recursion!

class BTNode: # TreeNode, modified for plain BT (no search stuff)

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

# the following functions (not methods!) are for original
#   list rep of binary tree given in DSP book,
#   followed by equivalent functions for the BTNode implementation (ending in 2):

def print_binary_tree2(root): # only works for node rep of a binary tree...
    for node in root: # note this relies on the __iter__method
        print(node)

def make_binary_tree(root_val):
    return [root_val, [], []] # single node, list rep

def make_binary_tree2(root_val):
    '''finish this'''
    root = BTNode(root_val) # single node, BTNode rep
    return root

def insert_left(root, new_child): # [rvalue,leftst, rightst]
    old_child = root.pop(1) # remove left child
    if len(old_child) > 1: # if it has children...
        root.insert(1, [new_child, old_child, []])
            # insert new node with new_child, having its left child as old_child
    else: # no children
        root.insert(1, [new_child, [], []])
            # insert new node with new_child, having no children
    return root

def insert_left2(root, new_child):
    old_child = root.left_child
    if old_child: # is there anything there?
        new_node = BTNode(new_child,old_child,None)
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
    old_child = root.right_child
    if old_child:  # is there anything there?
        new_node = BTNode(new_child, old_child, None)
        root.right_child = new_node
    else:
        root.right_child = BTNode(new_child)
    return root

def get_root_val(root):
    return root[0]

def get_root_val2(root):
    return root.value

def set_root_val(root, new_value):
    root[0] = new_value

def set_root_val2(root, new_value):
   root.value = new_value

def get_left_child(root):
    return root[1]

def get_left_child2(root):
    return root.left_child

def get_right_child(root):
    return root[2]

def get_right_child2(root):
    return root.right_child

# -----------------------------

def convert_to_list(a_tree : BTNode):
    ''' build and return list, assuming a_tree is a binary tree with node implementation'''
    # base case: no node
    if a_tree == None:  # empty node?
        return []
    else:
        return [
            a_tree.value,
            convert_to_list(a_tree.left_child),
            convert_to_list(a_tree.right_child)
            ]

def build_binary_tree_from_list(tree_list):
    '''
    build an equivalent BTNode binary tree from list rep tree_list
    '''

    if len(tree_list)==0:
        return None

    node = BTNode(tree_list[0]) # create new BTNode with data in tree_list

    node.left_child = build_binary_tree_from_list(tree_list[1])
    node.right_child = build_binary_tree_from_list(tree_list[2])

    return node

def format_list_rep(list_rep, indent):
    # print out list_rep, formatted as example below

    if len(list_rep) == 0: # empty
        # print (indent + "[],\\n")
        return indent + "[],\n"

    to_return = indent + "[" + str(list_rep[0]) + ",\n"
    # print (to_return)
    to_return += indent + "  " + format_list_rep(list_rep[1], indent+" ")
    # print (to_return)
    to_return += indent + "  " + format_list_rep(list_rep[2], indent+" ")
    # print (to_return)

    # print (to_return + indent + "],\\n")
    return to_return + indent + " ],\n"

def format_list_rep2(list_rep, indent):
    # print out list_rep, formatted as example below

    if len(list_rep) == 0: # empty
        # print (indent + "[],\\n")
        return indent + "[]"

    to_return = (
    f'''
    {indent}[{list_rep[0]},{format_list_rep2(list_rep[1],indent+"  ")},
    {format_list_rep2(list_rep[2],indent+"  ")}
    {indent}]''')
    return to_return

def main():
    '''
        the following code builds a binary tree using BinaryTreeNode '''
    newtree = make_binary_tree(47)
    print (newtree)
    insert_left(newtree,29)
    print (newtree)
    insert_right(newtree[1],13)
    print (newtree)

    # add some more examples....
    # repeat the above for this tree list, building a node-based BT:

    # [9,
    #    [11,
    #       [5,
    #          [4,
    #            [],
    #            []
    #          ],
    #          []
    #       ],
    #       []
    #    ],
    #    [7,
    #       [],
    #       [6,
    #          [],
    #          []
    #       ]
    #    ]
    #  ]


    tree2 = make_binary_tree2(9)
    node5 = BTNode(5)
    insert_left2(node5,4)
    node11 = BTNode(11)
    node11.left_child = node5
    tree2.left_child = node11

    node7 = BTNode(7)
    insert_right2(node7,6)
    tree2.right_child = node7
    
    # now convert the above node-based BT to list format

    tree_list = convert_to_list(tree2)
    print (tree_list)

   # finally iterate over the tree using for node in tree:...

    print_binary_tree2(tree2)

    # convert this back to a BTNode tree

    tree_list2 = convert_to_list(tree2)
    tree3 = build_binary_tree_from_list(tree_list2)
    print(convert_to_list(tree3))
    input(">>>")

# test the formatted list function

    tree_list3 = [47, [29,[13,[],[]],[]], []]
    result = format_list_rep(tree_list3,"")
    print ("formatted list: \n", result)
    input(">>>")
    result2 = format_list_rep2(tree_list3,"")
    print ("formatted list: \n", result2)



main()