# lab_4_0.py

# test of modified stack.Stack code with __str__implemented

import stack

def main():
    s = stack.Stack()
    s.push(1)
    s.push(2)

    print(str(s))

main()