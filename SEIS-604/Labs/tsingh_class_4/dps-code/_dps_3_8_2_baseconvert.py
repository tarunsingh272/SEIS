# _dps-3_8_2_baseconvert.py

# from pythonds3.basic import Stack

import stack as s

def base_converter(decimal_num, base):
    digits = "0123456789ABCDEF"
    rem_stack = s.Stack()

    while decimal_num > 0:
        rem = decimal_num % base
        rem_stack.push(rem)
        decimal_num = decimal_num // base

    new_string = ""
    while not rem_stack.is_empty():
        new_string = new_string + digits[rem_stack.pop()]

    return new_string

print(base_converter(25, 2))
print(base_converter(25, 16))
