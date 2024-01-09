#!/usr/bin/python3
"""
    This is the "0-add_integer" module

    The 0-add_integer module supplies one function, add_integer(a, b).
"""


def add_integer(a, b=98):
    # Checking that a, b are of type integers or floates only
    if not isinstance(a, int) or isinstance(a, float):
        raise TypeError("a must be an integer or b must be an integer")
    if not isinstance(b, int) or isinstance(b, float):
        raise TypeError("a must be an integer or b must be an integer")
    
    # Casting a, b to integers if they are floats
    a = int(a)
    b = int(b)

    # Perform addition and return result
    result = a + b
    return result
