# h4_1.py
# Tarun Singh

# add error detection and handling in postfix_eval()

import stack

def postfix_eval(postfix_expr):
    operand_stack = stack.Stack()
    token_list = postfix_expr.split()

    for token in token_list:
        if token in "0123456789":
            operand_stack.push(int(token))
        elif token in "+-/*":
            if(operand_stack.size() < 2):
                return "Error1"
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)

    if (operand_stack.size() == 1):
        return operand_stack.pop()
    # Missing operator
    return "Error2"

    return operand_stack.pop()


def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

def main():
    postfix1 = "7 8 + 3 2 + /"
    result = postfix_eval(postfix1)
    print("Result: ", result)

    postfix2 = "7 8 + 3 2 /"
    result = postfix_eval(postfix2)
    print("Result: ", result)

    postfix3 = "7 8 + 3 + /"
    result = postfix_eval(postfix3)
    print("Result: ", result)

main()