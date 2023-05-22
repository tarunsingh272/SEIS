__author__ = 'eric'

# pickteams.py:
#
#   program to print out random pairs of students from the list teams
#       containing each student's name

# put your name, favorite food, and favorite restaurant as comments below
# replace these with your own values:

# Tarun
# Raag Delhi Butter Chicken
# Raag Progressive Indian Cuisine

import random

unchosen = \
        [
        'Tarun Singh',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'h',
        'i',
        'j',
        'k',
        'l',
        'm',
        'n',
        'o',
        'p',
        'q',
        'r',
        's',
        't',
        'u',
        'v',
        'w',
        'x',
        'y',
        'z',
        'aa',
        'bb',
        'cc',
        'dd'
        ]

print ("\nTeam members:\n")

while True: # loop until break executed below

    if len(unchosen)==0:
        break # stop looping

    # pick a random location in the list, and print the name there
    place1 = random.randint(0,len(unchosen)-1)
    print (unchosen[place1],end=' ')

    # remove the name from that place
    unchosen.remove(unchosen[place1])

    # check if there's no more names: if so, break this loop
    if len(unchosen)==0:
        print()
        break # stop looping

    # pick a second random location, printing and removing the name there
    place2 = random.randint(0,len(unchosen)-1)
    print ("+", unchosen[place2])
    unchosen.remove(unchosen[place2])

