# h8_1.py

# from _dsp-6_6_1_bintree.py

def make_binary_tree(root):
    return [root, [], []]

def insert_left(root, new_child):
    old_child = root.pop(1)
    if len(old_child) > 1:
        root.insert(1, [new_child, old_child, []])
    else:
        root.insert(1, [new_child, [], []])
    return root

def insert_right(root, new_child):
    old_child = root.pop(2)
    if len(old_child) > 1:
        root.insert(2, [new_child, [], old_child])
    else:
        root.insert(2, [new_child, [], []])
    return root


def get_root_val(root):
    return root[0]

def set_root_val(root, new_value):
    root[0] = new_value

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]

def height(root):
    ''' finish this!'''
    left_height = 0
    right_height = 0

    if get_left_child(root) is not None:
        print(get_left_child(root))
        left_height = 1 + height(get_left_child(root))

    if get_right_child(root) is not None:
        print(get_right_child(root))
        right_height = 1 + height(get_right_child(root))

    return max(left_height, right_height)

def main():
    '''  '''
    # build this tree:
    #  [1,[2,[3,[],[]]],[4,[],[]]]

    newtree = make_binary_tree(1)
    print(newtree)
    insert_left(newtree, 2)
    print(newtree)
    insert_left(newtree[1], 3)
    print(newtree)
    insert_right(newtree, 4)
    print(newtree)
    print(get_root_val(newtree))
    print("Height of tree is :", height(newtree))
    # call your height function against the root and print the answer

main()

