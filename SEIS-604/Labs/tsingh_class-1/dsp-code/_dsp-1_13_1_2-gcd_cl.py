# _dsp-1_13_1_2-gcd_cl.py

def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n

print(gcd(20, 10))
