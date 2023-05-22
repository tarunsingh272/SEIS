# from DSP-1:  Fraction

# _dsp-1_13_1_2_3-fraction_class.py was file in Lab 1's class_1/dsp_code

def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
        cmnd = gcd(self.num, self.den)
        self.num = self.num // cmnd # Keep it int thats why //
        self.den = self.den // cmnd

    def __str__(self):
        return "{:d}/{:d}".format(self.num, self.den)

    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den

        return first_num == second_num

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

print(__name__)
if __name__ == "__main__":
    main()