# lab_6_1.py

'''

Write a pytest unit test function named test_grade
to test a function with the following specification.

Your asserts should check that the function produces an
appropriate value for each of the three postcondition cases.
'''

def grade(score):
    """Determines letter grade given a numeric score

    Precondition: 0 <= `score` <= 100
    Postcondition: Returns 'A' if 90 <= `score` <= 100,
      'B' if 80 <= `score` < 90, 'F' if 0 <= `score` < 80
    """
    if score >= 90 and score <= 100:
        return 'A'
    elif score >= 80 and score < 90:
        return 'B'
    else:
        return 'F'



def test_grade_A():
    assert grade(100) == 'A'

def test_grade_B():
    assert grade(89) == 'B'

def test_grade_F():
    assert grade(70) == 'F'

    pass # you finish this...
