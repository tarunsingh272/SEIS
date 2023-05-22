# seq_search.py

def seq_search(a_list, item):
    for i in a_list:
        if i == item:
            return True
    return False

import random
if __name__ == '__main__':
    test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(seq_search(test_list, 3))
    print(seq_search(test_list, 13))
