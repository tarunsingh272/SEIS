# (complicated) HTT1 example

def fibonacci(N):
    fn_1 = 0
    fn_2 = 1
    fn = 0
    if N < 0:
        fn = 'Please return a number >= 0'
    else:
        if N == 0:
            fn = 0
        else:
            for i in range(N):
                fn = fn_1 + fn_2
                fn_2 = fn_1
                fn_1 = fn
    return fn

def fibturtle(boxnumber):
    import turtle

    fibsquare = turtle.Turtle()
    wn = turtle.Screen()
    fibsquare.hideturtle()
    fibsquare.right(90)
    fibsquare.speed(0)
    possave = fibsquare.position()
    headingsave = fibsquare.heading()

    for i in range(1, boxnumber + 1):
        fibnumber = fibonacci(i)
        fibsquare.begin_fill()
        #time to draw squares.  6 iterations to set turtle back in proper spot
        for j in range(1, 7):
            fibsquare.forward(fibnumber * 5) # multipled by 5 to make image viewable
            fibsquare.fillcolor('light yellow')
            if j != 6:
                if j == 5:
                    fibsquare.end_fill()
                fibsquare.left(90)
            else:
                # time to set the middle text
                fibsquare.up()
                possave = fibsquare.position()
                headingsave = fibsquare.heading()
                # set back to original location and ready for gridlines
                fibsquare.setposition(possave)
                fibsquare.setheading(headingsave + 180)
                fibsquare.color('pink')
                #first gridlines
                for grid in range(1, fibnumber):
                    fibsquare.forward(grid * 5)
                    fibsquare.right(90)
                    fibsquare.forward(1)
                    fibsquare.down()
                    fibsquare.forward(fibnumber * 5 - 2)
                    fibsquare.up()
                    fibsquare.setposition(possave)
                    fibsquare.setheading(headingsave + 180)
                #second gridlines
                for grid in range(1, fibnumber):
                    fibsquare.right(90)
                    fibsquare.forward(grid * 5)
                    fibsquare.left(90)
                    fibsquare.forward(1)
                    fibsquare.down()
                    fibsquare.forward(fibnumber * 5 - 2)
                    fibsquare.up()
                    fibsquare.setposition(possave)
                    fibsquare.setheading(headingsave + 180)
                #text in middle of square
                fibsquare.color('black')
                fibsquare.setheading(headingsave + 180)
                fibsquare.forward(fibnumber * 2.5)
                fibsquare.right(90)
                fibsquare.forward(fibnumber * 2.5)
                fibsquare.write(str(fibnumber), font=("Calibri", fibnumber, "normal"), align="center")
                #finish out
                fibsquare.setposition(possave)
                fibsquare.setheading(headingsave)
                fibsquare.down()


    wn.exitonclick()

def main():
    fibturtle(int(input('Please enter how many fib boxes you want to see: ')))

if __name__ == "__main__":
    main()