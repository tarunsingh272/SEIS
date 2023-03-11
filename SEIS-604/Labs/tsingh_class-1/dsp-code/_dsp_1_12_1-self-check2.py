# _dsp-1_12_1-self-check2.py
# soln to Self Check Challenge

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

def generate2(n,best_so_far):
    '''
    Generate a random string of letters of passed length n,
    just changing one of the non-matches in best_so_far
    '''
    to_return = ''
    alter_done = False
    for i in range(n):
        if alter_done or best_so_far[i]==sentence[i]:
            to_return += best_so_far[i]
        else:
            to_return += random.choice(string.ascii_lowercase + " ")
            alter_done = True
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
    counter = 0
    best_so_far = 0
    best_str = '-' * len(sentence) # no matches to start
    while True:
        counter += 1
        guess = generate2(len(sentence),best_str)
        result = score(guess)
        print("guess, score", guess, result)
        if result > best_so_far:
            best_so_far = result
            best_str = guess
        if guess == sentence:
            print ("got it! in ", counter, "guesses.")
            break
        if counter % 100 == 0:
            print ("best so far:",best_str,"with score",best_so_far)
run_it()