# h6_1.py
#

import turtle as t

moxie = t.Turtle()
wn = t.Screen()

N = 3
side = 200

def box(t,side,depth):
    if depth == 0:
        return
    for ct in range(4):
        t.forward(side)
        t.left(90)

    t.left(90)
    t.forward(side)
    t.right(90)
    t.forward(side//4)
    box(t,side//2,depth-1)

moxie.up()
moxie.goto(-100,-100)
moxie.down()
box(moxie,side,N)
wn.exitonclick()
