# Fraction.py
# Tarun Singh

# part of H1: make all your changes to this file,
#   which is then imported into your test code

def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return "{:d}/{:d}".format(self.num, self.den)

    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den

        return first_num == second_num

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den \
        + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        cmmn = gcd(new_num, new_den)
        return Fraction(new_num // cmmn, new_den // cmmn)

    def show(self):
        print("{:d}/{:d}".format(self.num, self.den))

    def get_den(self):
        return self.den

    def get_num(self):
        return self.num

    def __mul__(self, other_fraction):
        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other_fraction):
        new_num = self.num * other_fraction.den
        new_den = self.den * other_fraction.num
        common = gcd(abs(new_num), abs(new_den))
        return Fraction(new_num // common, new_den // common)

    def __sub__(self, other_fraction):
        new_num = (self.num * other_fraction.den) - (self.den * other_fraction.num)
        new_den = self.den * other_fraction.den
        common = gcd(abs(new_num), abs(new_den))
        return Fraction(new_num // common, new_den // common)

    def __ne__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = self.den * other_fraction.num
        return first_num != second_num

    def __gt__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = self.den * other_fraction.num
        return first_num > second_num

    def __ge__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = self.den * other_fraction.num
        return first_num >= second_num

    def __lt__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = self.den * other_fraction.num
        return first_num < second_num

    def __le__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = self.den * other_fraction.num
        return first_num <= second_num

    def __repr__(self):
        print("__repr__ called")
        return '%s(%r)' % (self.__class__, self.__str__())

