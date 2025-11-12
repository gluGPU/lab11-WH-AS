"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

# First example
def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def log(a, b):
    if a < 0:
        raise ValueError
    else:
        return math.log(b, a)
    
def exp(a, b):
    return a ** b


