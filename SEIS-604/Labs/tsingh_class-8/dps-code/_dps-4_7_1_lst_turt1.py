# the following works in the Jupyter Notebook, but won't terminate:  try it!

# _dsp-4_7_1-lst_turt1.py

import turtle

def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len - 5)


my_turtle = turtle.Turtle()
my_win = turtle.Screen()
draw_spiral(my_turtle, 100)
#turtle.done()
#try:
#    turtle.bye()
#except:
#    print("bye")

my_win.exitonclick()

