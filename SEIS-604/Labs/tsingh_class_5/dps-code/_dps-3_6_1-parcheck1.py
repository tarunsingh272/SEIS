# _dps-3_6_1_parcheck1.py
import Stack as st

def par_checker(symbol_string):
    s = st.Stack()
    for symbol in symbol_string:
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            else:
                s.pop()

    return s.is_empty()


print(par_checker("((()))"))  # expected True
print(par_checker("((()()))"))  # expected True
print(par_checker("(()"))  # expected False
print(par_checker(")("))  # expected False
