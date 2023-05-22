# htt_20_3_1-ac_round6_3.py

def round6(num):
    return int(num + .4)

# ---- automated unit test ----

result = round6(9.7)
if result == 10:
    print("Test 1: PASS")
else:
    print("Test 1: FAIL")

result = round6(8.5)
if result == 8:
    print("Test 2: PASS")
else:
    print("Test 2: FAIL")
