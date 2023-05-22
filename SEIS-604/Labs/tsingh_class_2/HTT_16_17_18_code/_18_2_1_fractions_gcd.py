#
# HTT Ch 18 code example:
#
# Section 18.2, example 1: fractions_gcd.py
#
def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn

    return n

print(gcd(12, 16))
