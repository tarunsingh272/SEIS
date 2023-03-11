# _dsp-1_12_1-self-check1.py

# do this in PyCharm...

sentence = "methinks it is like a weasel"

import string
import random
def generate(n):
    '''
    Generate a random string of letters of passed length n
    '''
    to_return = ''
    for i in range(n):
        to_return += random.choice(string.ascii_lowercase + " ")
    return to_return

def score(guess):
    '''
    Compare guess to sentence and return # of equal chars
    '''
    count = 0
    for ind in range(len(guess)):
        if guess[ind]==sentence[ind]:
            count += 1
    return count

def run_it():
    '''
    repeatedly generate a guess until it matches sentence
    '''
    pass

run_it()