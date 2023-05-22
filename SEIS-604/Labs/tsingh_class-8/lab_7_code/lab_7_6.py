# lab 7-6:

# Work on implementing the Koch snowflake curve

import turtle

def koch(t, side, depth):
    ''' finish me '''
    if depth==0:
        t.forward(side)
        return

    koch(t,side//4,depth-1)
    t.left(60)
    koch(t,side//4, depth-1)
    t.right(120)
    koch(t,side//4,depth-1)
    t.left(60)
    koch(t,side//4,depth-1)

def hilbert(t, side, depth):
    ''' try this if we have time...'''

def main():
    moxie = turtle.Turtle()
    wn = turtle.Screen()
    moxie.speed(0)
    moxie.up()
    moxie.back(400)
    moxie.down()
    koch(moxie,4096,6)

    wn.exitonclick()

main()

