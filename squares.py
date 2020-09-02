import turtle
import math
PEN_WIDTH = 1
MARGIN = 20

def init():
    """
    The following initialization steps create a square
    window that uses most of the screen, regardless
    of the resolution of the display it runs on.  This
    avoids any trouble with sizing the window.

    :param size: a resolution parameter so that
                 the coordinate system ranges from -20 to size+20 in both dimensions.
    :param speed: a number between 1 and 10 indicating turtle movement speed
                  0 => don't show animation; just draw
    :post: turtle is at -150,-150, facing east (0 degrees), pen up
    """

    turtle.reset()
    smaller_dim = min( turtle.window_height(), turtle.window_width() )
    turtle.setup( smaller_dim, smaller_dim )
    turtle.down()
    #turtle.hideturtle()
    turtle.speed(5)
    turtle.pensize( PEN_WIDTH )
    turtle.penup()
    turtle.setposition( -150, -150 )

def drawsquares(sidelength, depth):
    turtle.pendown()
    if depth <= 0:
        return
    for i in range(2):
        if depth % 2 == 0:
            turtle.color("blue")
        else:
            turtle.color("orange")
        turtle.forward(sidelength)
        turtle.left(90)
        turtle.forward(sidelength/2)
        turtle.left(45)
        newsidelength = math.sqrt(math.pow(sidelength,2)/8)
        drawsquares(newsidelength, depth-1)
        turtle.right(45)
        turtle.forward(sidelength/2)
        turtle.left(90)


def main() -> None:
    depth = input("What depth?")
    init()
    drawsquares(300, int(depth))
    turtle.mainloop()


if __name__ == '__main__':
    main()