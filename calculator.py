"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

# First example
def add(a, b): 
    pass

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b / a

def log(a, b):
    if b < 0:
        raise ValueError
    else:
        return math.log(b, a)

def exp(a, b):
    return a**b