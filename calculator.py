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

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b / a
<<<<<<< HEAD

=======
    
>>>>>>> 5393869171c610b975b38b7d9a696f1ca59a2826
def log(a, b):
    if a < 0:
        raise ValueError
    else:
        return math.log(b, a)
    
def exp(a, b):
<<<<<<< HEAD
    return a ** b
    
=======
    return a**b
>>>>>>> 5393869171c610b975b38b7d9a696f1ca59a2826
