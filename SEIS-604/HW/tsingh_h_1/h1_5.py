# h1_5.py
# Tarun Singh

import fraction

# modify fraction.py, then import here and test it as specified:

# When run, your program should create a Fraction with value 46/47,
#   then print out its numerator and denominator using
#   get_den() and get_num().

from fraction import Fraction

x = Fraction(46, 47)
x.show()
print("Denominator is: ", x.get_den())
print("Numerator is: ", x.get_num())

# fraction.Fraction is the class
