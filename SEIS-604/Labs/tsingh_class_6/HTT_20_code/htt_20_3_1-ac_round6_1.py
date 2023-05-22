# htt_20_3_1-ac_round6_1.py

def round6(num):
    """returns num rounded to nearest int if fractional part is >= .6"""

    return int(num + .6)

# ----- test program -------

x = float(input('Enter a number:'))
result = round6(x)
print('Result: ', result)
