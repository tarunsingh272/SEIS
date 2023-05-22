# h7_3.py

# implement the recursive H-curve as described in the H7 handout
import turtle

def drawH(t, d, len):

    if d > 0:
        # start in center of H, move to upper right
        t.forward(len / 2)
        t.left(90)
        t.forward(len / 2)
        t.right(90)
        drawH(t, d - 1, len / 2)

        # move to lower right of H
        t.right(90)
        t.forward(len)
        t.left(90)
        drawH(t, d - 1, len / 2)

        # move to upper left of H
        t.left(90)
        t.forward(len / 2)
        t.left(90)
        t.forward(len)
        t.right(90)
        t.forward(len / 2)
        t.right(90)
        drawH(t, d - 1, len / 2)

        # move to lower left of H
        t.right(90)
        t.forward(len)
        t.left(90)
        drawH(t, d - 1, len / 2)

        # return to center of H
        t.left(90)
        t.forward(len / 2)
        t.right(90)
        t.forward(len / 2)


def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    d = int(input("Enter the d"))
    len = float(input("Enter the length of side"))
    drawH(t, d, len)
    my_win.exitonclick()

main()