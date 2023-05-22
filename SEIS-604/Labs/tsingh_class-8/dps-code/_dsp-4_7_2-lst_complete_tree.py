# _dsp-4_7_2-lst_complete_tree.py

# Run this in PyCharm...

import turtle
import random

def tree(branch_len, t):
    colors = ["brown", "green"]
    t.pensize(branch_len//10)
    if branch_len < 15:
        t.pencolor(colors[0])
    else:
        t.pencolor(colors[1])

    if branch_len > 5:
        t.forward(branch_len)
        angle = random.randint(15,45)
        t.right(angle)
        tree(branch_len - 15, t)
        t.left(2*angle)
        tree(branch_len - 15, t)
        t.right(angle)
        t.backward(branch_len)

def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t)
    my_win.exitonclick()

main()
