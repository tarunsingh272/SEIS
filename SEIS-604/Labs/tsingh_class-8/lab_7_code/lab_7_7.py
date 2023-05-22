# lab 7-7:

# Work on implementing the Hilbert space filling curve

import turtle
def hilbert_ccw(t, depth,side):
    if depth == 0:
        return

    t.right(90)
    hilbert_cw(t, depth - 1, side)
    t.forward(side)
    t.left(90)
    hilbert_ccw(t, depth - 1, side)
    t.forward(side)
    hilbert_ccw(t, depth - 1, side)
    t.left(90)
    t.forward(side)
    hilbert_cw(t, depth - 1, side)
    t.right(90)

def hilbert_cw(t, depth, side):
    ''' finish me '''
    if depth==0:
        return

    t.left(90)
    hilbert_ccw(t,depth-1,side)
    t.forward(side)
    t.right(90)
    hilbert_cw(t,depth-1,side)
    t.forward(side)
    hilbert_cw(t,depth-1,side)
    t.right(90)
    t.forward(side)
    hilbert_ccw(t,depth-1,side)
    t.left(90)

def hilbert(t, depth, side, angle):
    if depth == 0:
        return

    t.right(angle)
    hilbert(t, depth - 1, side, angle)
    t.forward(side)
    t.left(angle)
    hilbert(t, depth - 1, side, angle)
    t.forward(side)
    hilbert(t, depth - 1, side, angle)
    t.left(angle)
    t.forward(side)
    hilbert(t, depth - 1, side)
    t.right(angle)

def main():
    moxie = turtle.Turtle()
    wn = turtle.Screen()
    moxie.speed(0)
    moxie.up()
    moxie.back(400)
    moxie.left(90)
    moxie.back(400)
    moxie.right(90)
    moxie.down()

    hilbert(moxie,6,10,90)

    wn.exitonclick()

main()

