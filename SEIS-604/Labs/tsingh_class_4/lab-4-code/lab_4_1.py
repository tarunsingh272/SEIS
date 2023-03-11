# lab_4_1.py

# modified version of infix_to_postfix(), with added
#   code printing out a trace of the executing code.

# we'll run this and observe how the algorithm works

import stack

def infix_to_postfix(infix_expr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    op_stack = stack.Stack()
    postfix_list = []
    token_list = infix_expr.split()

    for token in token_list:
        print (f"\nProcessing token '{token}' in {token_list}")
        print (f"op_stack is {op_stack}")

        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
            print(f"\tAppended operand '{token}' to postfix_list: {postfix_list}")
        elif token == "(":
            op_stack.push(token)
            print(f"\tPushed '(' to {op_stack}")
        elif token == ")":
            print ("\tEnd of parenthesized expression: popping op_stack and transferring to postfix_list until matching ')' found...")
            top_token = op_stack.pop()
            while top_token != "(":
                print ("\tAppending {top_token} to ")
                postfix_list.append(top_token)
                top_token = op_stack.pop()
            print(f"\tpostfix_list now: {postfix_list}")
            print(f"\top_stack now: {op_stack}")
        else: # token is an operator: process
            print("\tToken is an operator, so popping op_stack and transferring to postfix_list:")
            # print ("do while op_stack top has greater precedence than current token...")
            while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
                print(f'\ttop of op_stack {op_stack.peek()} has higher precedence than next token {token}')
                postfix_list.append(op_stack.pop())
            print (f"\tnow either op_stack empty or top of op_stack has lesser prec than token")
            op_stack.push(token)
            print(f"\tpostfix_list now: {postfix_list}")
            print(f"\top_stack now: {op_stack}")

    print (f"finally: empty op_stack and transfer to postfix_list: ")
    while not op_stack.is_empty():
        print (f"moving {op_stack.peek()} to postfix_list")
        postfix_list.append(op_stack.pop())
    print ("Done!")
    return " ".join(postfix_list)

print(infix_to_postfix("A * B / C"))

# print(infix_to_postfix("A * B + C * D"))
# print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
