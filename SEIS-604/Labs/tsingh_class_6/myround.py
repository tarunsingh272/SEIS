# test_htt20_7_1-round6.py

# pytest runs files with prefix test_:
#   each function with prefix test_ then is executed as part of the test

def round6(num: float) -> int:
    """This function has a bug in it"""
    return int(num + .6)

# ---- automated unit test ----

def test_round6():
    assert round6(9.7) == 10
    assert round6(8.5) == 8

