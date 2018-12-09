# Hyperbolic Turtle Graphics

Hyperbolic Turtle Graphics is a LOGO type program where the turtle moves in the Poincaré disk model of the hyperbolic plane.

Right now the code is terrible, including use of a global variable named i (which will conflict with typical variables used in for loops).   

However, it works and can be used to produce some nice pictures and learn some geometry.

## Example usage

 Example usage:

 From IDLE

        >>> import os
        >>> os.chdir('the directory containing hturtle.py')
        >>> import hturtle
        >>> hturtle.forward(1)
        >>> hturtle.right(90)
        >>> hturtle.forward(1)
        >>> hturtle.right(90)
        >>> hturtle.forward(1)
        >>> hturtle.right(90)
        >>> hturtle.forward(1)
        >>> hturtle.right(90)
        >>> hturtle.right(90)


 This generates the file 'screenshot1.eps' containing the following image:

 ![screenshot1.svg](/screenshot1.svg)

## Relationship to the turtle standard library

 This program is built on the turtle library which is imported as turtle.  For example:

        >>> hturtle.reset()
        >>> hturtle.turtle.pencolor('brown')
        >>> hturtle.regularwalk(1,90,20)
        >>> hturtle.screenshot('screenshot2')

 ![screenshot2.svg](/screenshot2.svg)

## Other functions

 There are several functions in hturtle.py which are for internal use.  The ones meant for interacting with the turtle are: reset, right, randomwalk, regularwalk, screenshot, side, forward, path, and allwalk.

        >>> hturtle.reset()
        >>> for s in range(5,20):
		hturtle.regularwalk(hturtle.side(s),90,s)
        >>> hturtle.screenshot('screenshot3')

 ![screenshot3.svg](/screenshot3.svg)


        >>> hturtle.reset()
        >>> hturtle.turtle.pencolor('blue')
        >>> hturtle.randomwalk(0.1,[-90,0,90,180],1000)
        >>> hturtle.screenshot('screenshot4')

 ![screenshot4.svg](/screenshot4.svg)

# Have fun!

