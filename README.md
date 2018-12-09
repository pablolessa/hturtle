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

 ![screenshot1.eps](/screenshot1.eps)

## Relationship to the turtle standard library

 This program is built on the turtle library which is imported as turtle.  For example:

        >>> hturtle.reset()
        >>> hturtle.turtle.pencolor('brown')
        >>> hturtle.regularwalk(1,90,20)
        >>> hturtle.screenshot('screenshot2')

 ![screenshot2.eps](/screenshot2.eps)

## Other functions

 There are several functions in hturtle.py which are for internal use.  The ones meant for interacting with the turtle are:

 hturtle.reset()
 hturtle.right(angle in degrees)
 hturtle.randomwalk(step size, list of angles, number of steps)
 hturtle.regularwalk(step size, angle, number of steps)
 hturtle.screenshot(name to which .eps will be added)
 hturtle.side(number of sides)
 hturtle.forward(distance)
 hturtle.path(step size, list of turning angles)
 hturtle.allwalk(number of steps, step size, list of angles)

        >>> hturtle.reset()
        >>> for s in range(5,20):
		hturtle.regularwalk(hturtle.side(s),90,s)
        >>> hturtle.screenshot('screenshot3')

 ![screenshot3.eps](/screenshot3.eps)

# Have fun!

