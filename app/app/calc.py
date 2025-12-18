"""
calculator functions 
"""


def add(x, y):
    """add two numbers and return the result"""
    return x + y


def subtract(x, y):
    """subtract two numbers and return the result"""
    if x > y:
        return x - y
    else:
        return y - x
