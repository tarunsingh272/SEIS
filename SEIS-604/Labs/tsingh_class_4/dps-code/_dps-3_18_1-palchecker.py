# _dps-3_18_1_palchecker.py
# can also import deque from book's module

# from pythonds3.basic import Deque

import deque as d
def pal_checker(a_string):
    char_deque = d.Deque()

    for ch in a_string:
        char_deque.add_rear(ch)

    while char_deque.size() > 1:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if first != last:
            return False

    return True

print(pal_checker("lsdkjfskf"))
print(pal_checker("radar"))
print(pal_checker("level"))
