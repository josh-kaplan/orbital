#!/usr/bin/env python
from __future__ import division
from math import pi
from sympy import *

# Symbols
M, E, e, p = symbols('M E e p')

# Variable substitution - These are optional
M = 1/2 #p/2
e = .3

# The function and it's derivative
func = E - e*sin(E) - M
dfunc = diff(func, E)

def f(x):
    return func.subs(E, x)

def df(x):
    return dfunc.subs(E, x)

def newtons_method():
    x = -2*pi           # initial guess
    iters = 3       # number of iterations
    for i in xrange(1, iters+1):
        x = x + f(x)/df(x)
    print x

if __name__ == '__main__':
    newtons_method()

