# htt20_2_1-ac_sumnums_1.py

def sumnums(lo, hi):
    """returns the sum of the numbers in the range [lo..hi]"""

    sum = 0
    for i in range(lo, hi+1):
        sum += i
    return sum

print(sumnums(1, 3))
print(sumnums(3, 1))
