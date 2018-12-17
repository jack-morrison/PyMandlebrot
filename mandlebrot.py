#!/usr/bin/env python3

## Topics:
## - The Mandlebrot Set
## - Python's complex() built-in
## - numpy arrays & linspace iteration
## - matplotlib.pyplot.imshow()

## The Mandlebrot Set:
##     The set of compelx numbers c for which the function
##                     f(z) = z^2 + c
##     does not diverge when iterated from z = 0.

import matplotlib.pyplot as plt
import numpy

## If a value is diverging (out of set), the number of iterations before
## divergence is returned. If a value is not diverging (in set), the maximum
## number of iterations is reached and returned.
def mandlebrot(real, imaginary, iterations):
    c = complex(real, imaginary)
    z = 0.0j

    ## let's say a value greater than 10 is diverging...
    ## TODO: what's a better way to define the divergence threshold?
    threshold = 10
    for iter in range(iterations):
        z = (z*z) + c

        if (z.real*z.real + z.imag*z.imag > threshold):
            return iter

    return iterations


## Represent the plot as a 2D array
cols = 2000
rows = 2000
canvas = numpy.zeros([rows, cols])

## Increasing maxIterations increases confidence in divergence.
maxIterations = 100

for row, real in enumerate(numpy.linspace(-2, 2, num=rows)):
    for col, imaginary in enumerate(numpy.linspace(-2, 2, num=cols)):
        canvas[row, col] = mandlebrot(real, imaginary, maxIterations)


## TODO: How can I create canvas such that there's no need to transpose it?
plt.imshow(canvas.T, cmap='coolwarm', extent=[-2,2,-2,2])
plt.xlabel('real')
plt.ylabel('imaginary')
plt.show()
