# lab_4_3.py

# this is annotated version of algorithm

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
            print(f"\tPushed op '(' to {op_stack}")
        elif token == ")":
            print ("\tEnd of parenthesized expression: ")
            print ("Repeatedly pop op_stack and transfer to end of postfix_list until matching '(' found...")
            top_token = op_stack.pop()
            while top_token != "(":
                print ("\tappending {top_token} to end of postfix_list")
                postfix_list.append(top_token)
                top_token = op_stack.pop()
            print(f"\tpostfix_list now: {postfix_list}")
            print(f"\top_stack now: {op_stack}")
        else: # token is an operator: process
            print("\ttoken is an operator, so popping op_stack and transferring to postfix_list:")
            print ("do while op_stack top has greater precedence than current token...")
            while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
                print(f'\ttop of op_stack {op_stack.peek()} has higher precedence than next token {token}')
                print(f'Send {op_stack.peek()} to end of postfix_list')
                postfix_list.append(op_stack.pop())
            print (f"\tnow either op_stack empty or top of op_stack has <= prec than token")
            print (f"\t  moving {token} to op_stack...")
            op_stack.push(token)
            print(f"\tpostfix_list now: {postfix_list}")
            print(f"\top_stack now: {op_stack}")

    print (f"finally: empty op_stack and transfer to end of postfix_list: ")
    while not op_stack.is_empty():
        print (f"moving {op_stack.peek()} to end of postfix_list")
        postfix_list.append(op_stack.pop())
    print ("done!")
    return " ".join(postfix_list)

print(infix_to_postfix("A * B + C * D"))
# print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
