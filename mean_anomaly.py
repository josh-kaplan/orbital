#!/usr/bin/env python
"""
mean_anomaly.py

Josh Kaplan
contact@joshkaplan.org

Solves for the mean anomaly in terms of symbolic variables using Newtons's
Method. Those variables can be replaced (see "variable substitution" below) to
find an exact solution. Note that this script only uses a maximum number of
iterations (see "iterations" in the "newtons_method" function) rather than a
tolerance for ease of use with symbolic variables.

"""
from __future__ import division, print_function
from math import pi
from sympy import *

# Symbols
M, E, e, p = symbols('M E e p')

# Variable substitution - These are optional
M = p/2
e = .3

# The function and it's derivative
func = E - e*sin(E) - M
dfunc = diff(func, E)

def f(x):
    return func.subs(E, x)

def df(x):
    return dfunc.subs(E, x)

def newtons_method():
    x = -2*pi     # initial guess
    iters = 2     # number of iterations
    for i in range(1, iters+1):
        x = x + f(x)/df(x)
    print(x)

if __name__ == '__main__':
    newtons_method()

