# lab_5_1.py

# Modify the following to ignore spaces:  DSP-3.27 Exercise 1

# Try to also ignore all characters other than lower case letters.

# Then add your own code that demonstrates its correct behavior

import deque
import string

def pal_checker(a_string):
    char_deque = deque.Deque()

    for ch in a_string:
        if ch.isalpha():
            char_deque.add_rear(ch.lower())
        if ch != ' ':
            char_deque.add_rear(ch)

    while char_deque.size() > 1:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if first != last:
            return False

    return True

print(pal_checker("lsdkjfskf"))
print(pal_checker("radar"))

# add more tests that check if it handles blanks correctly

print(pal_checker("a man, a plan a canal panama"))
print(pal_checker("A man, a plan, a canal - Panama"))
# a man, a plan, a canal: panama
