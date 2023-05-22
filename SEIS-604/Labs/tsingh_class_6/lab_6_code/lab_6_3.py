# lab_6_3.py

# add the relational operators >, <, >=, <=, != to Fraction
# == (__eq__) is already done for you
# try to write tests before adding an operator

def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
        cmnd = gcd(self.num,self.den)
        self.num = self.num // cmnd
        self.den = self.den // cmnd

    def __str__(self):
        return "{:d}/{:d}".format(self.num, self.den)

    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den

        return first_num == second_num

    def __ne__(self, other_fraction):
        return not self == other_fraction

    def __gt__(self, other_fraction):
        f1 = self.num / self.den
        f2 = other_fraction.num / other_fraction.den
        return f1 > f2

    def __ge__(self, other_fraction):
        f1 = self.num / self.den
        f2 = other_fraction.num / other_fraction.den
        return f1 >= f2

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        # cmmn = gcd(new_num, new_den)
        return Fraction(new_num, new_den)

    def show(self):
        print("{:d}/{:d}".format(self.num, self.den))


def main():
    x = Fraction(1, 2)
    x.show()
    y = Fraction(2, 3)
    print(y)
    print(x + y)
    print(x == y)

# print (__name__)
# if __name__ == "__main__": # are we calling this as a program?
#     main()

def test_one():
    f = Fraction(1,47)
    assert f == f

def test_eq_1():
    f = Fraction(1, 47)
    f2 = Fraction(1, 47)
    assert f == f2

def test_ne_1():
    f = Fraction(1, 47)
    f2 = Fraction(1, 2)
    assert f != f2

def test_gt_1():
    f = Fraction(1, 47)
    f2 = Fraction(0, 47)
    assert f > f2

def test_ge_1():
    f = Fraction(1, 47)
    f2 = Fraction(0, 47)
    assert f >= f2

def test_lt_1():
    f = Fraction(1, 47)
    f2 = Fraction(0, 47)
    assert f2 < f

def test_le_1():
    f = Fraction(1, 47)
    f2 = Fraction(0, 47)
    assert f2 <= f