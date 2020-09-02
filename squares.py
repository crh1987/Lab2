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
    turtle.setposition( -150, -150 ) #make it more centered on the screen

def drawsquares(sidelength, depth):
    """
       Takes sidelength and depth and draws that many squares in a given pattern

        :param sidelength: how long the first square's sides are, kept at 300
        :param depth: how many times the code is repeated/ recursively called
        :post: turtle is at -150,-150, facing east (0 degrees), pen down
        """

    turtle.pendown() #start with down pen
    if depth <= 0:      #base case
        return
    for i in range(2):      #for loop to repeat twice
        if depth % 2 == 0:      #changing colors: evens are blue and odd depths are orange
            turtle.color("blue")
        else:
            turtle.color("orange")
        turtle.forward(sidelength)      #start on first square
        turtle.left(90)
        turtle.forward(sidelength/2) #continue to where next square starts
        turtle.left(45)         #start drawing next square at 45 degree angle
        newsidelength = math.sqrt(math.pow(sidelength,2)/8)     #using pythagorean's theorem, the sidelength should be sqrt(x^2/8)
        drawsquares(newsidelength, depth-1)     #recursively call so that this process is repeated until depth is zero
        turtle.right(45)        #after all of the above code resolves, begin finishing the rest of the squares, orient right 45 degrees to offset the leftward 45 degree turn
        turtle.forward(sidelength/2)
        turtle.left(90)


def main() -> None:
    depth = input("What depth?")
    init()
    drawsquares(300, int(depth))
    turtle.mainloop()


if __name__ == '__main__':
    main()