import turtle
from numpy import *
from math import pi,acos,acosh,sin
import random

_radius = 200 #radius of the disk we're using to represent the hyperbolic plane
_i = complex(0,1)
_mstate = matrix([[1,0],[0,1]])   #matrix codifying current position/direction


def reset():
    global _mstate,_radius
    _mstate = matrix([[1,0],[0,1]])
    turtle.reset()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(0,-_radius)
    turtle.pendown()
    turtle.circle(_radius,360)
    turtle.penup()
    turtle.home()
    turtle.pendown()

def home():
    global _mstate
    _mstate = matrix([[1,0],[0,1]])
    turtle.home()
    
    
def FD(t):
    '''Right multiplication by this makes the mstate advance t along a geodesic.'''
    A = matrix([[exp(t/2.),0],[0,exp(-t/2.)]])
    return A

def RT(t):
    '''Right multiplication by this rotates the mstate clockwise t radians.'''
    t2 = t/(2.0)
    s = sin(t2)
    c = cos(t2)
    A = matrix([[c,-s],[s,c]])
    return A

def matrix2upper(A):
    '''Convert a matrix to a point/vector in the upper half-plane model.'''
    global _i
    a,b,c,d = A[0,0],A[0,1],A[1,0],A[1,1]
    det = a*d - c*b
    v = det*_i/((c*_i+d)**2)
    return (a*_i+b)/(c*_i+d), v

def upper2disk(X):
    z,v = X
    global _i,_radius
    '''Convert from the upper half-plane model to the disk of our given radius.'''
    znew = _radius*(z-_i)/(z+_i)
    vnew = v*2*_radius*_i/((z+_i)**2)
    return znew,vnew

def matrix2disk(A):
    '''Convert from matrix to the disk model.'''
    return upper2disk(matrix2upper(A))

def right(t):
    global _mstate
    '''Turn right t degrees'''
    turtle.right(t)
    r = t*2*pi/360
    _mstate = _mstate*RT(r)

def angle(v,w):
    '''Return the angle in degrees between two vectors'''
    v = v/abs(v)
    w = w/abs(w)
    return 360*arccos((v*w.conjugate()).real)/(2*pi)

def forward(t):
    '''Move the turtle forward a distance t along a hyperbolic geodesic.'''
    global _mstate
    z0,v0  = matrix2disk(_mstate)
    _mstate = _mstate*FD(t)
    z1,v1 = matrix2disk(_mstate)
    a = angle(v0,v1)
    aradians = 2*pi*a/360
    factor = sin(aradians/2.) #used for calculating the radius of the circle
    side = ((z1-z0)/v0).imag # if positive the destination is to the left
    if factor != 0 and side != 0:
        r = sign(side)*abs(z1-z0)/(2*factor)
        turtle.circle(r,extent=a)
    turtle.goto(z1.real,z1.imag)

def randomwalk(stepsize, angles, numsteps):
    '''Goes forward stepsize then turns right a random choice from angles. Repeats numsteps times.'''
    for k in range(numsteps):
        forward(stepsize)
        right(random.choice(angles))

def regularwalk(stepsize,angle, numsteps):
    '''Goes forward stepsize then turns right angle.  Repeats numsteps times.'''
    for i in range(numsteps):
        forward(stepsize)
        right(angle)

def screenshot(name):
    '''Saves a screenshot to name.eps'''
    turtle.getcanvas().postscript(file=name+'.eps')

def side(n = 5):
    '''Returns the side of the regular polygon with 90 degree interior angles and n sides.'''
    return 2*acosh(cos(pi/n)/sin(pi/4))


def path(d,angles):
    '''Trace a path with steps of length d and given angles.'''
    for a in angles:
        right(a)
        forward(d)

def allwalk(d,length,angles,word=[]):
    '''Trace all paths of given length and angles.'''
    if length != 0:
        for letter in angles:
            word.append(letter)
            allwalk(d,length-1,angles,word)
            word.pop()
    else:
        path(d,word)
        turtle.penup()
        home()
        turtle.pendown()
  
reset()
