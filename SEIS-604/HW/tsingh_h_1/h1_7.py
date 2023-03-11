# h1_7.py
# Tarun Singh

# modify fraction.py, then import here and test it as specified:

# When run, your program should create two Fraction instances
#   representing 1/2 and 1/6, then print each of the expressions
#   1/2 - 1/6, 1/2 * 1/6, and 1/2 / 1/6 thus demonstrating your
#   implementations of __sub__, __mul__, and __truediv__ are all correct.

from fraction import Fraction

x = Fraction(1,2)
y = Fraction(1,6)

print(x+y)
print(x-y)
print(x*y)
print(x/y)

# fraction.Fraction is the class
