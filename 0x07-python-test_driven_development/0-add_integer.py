#!/usr/bin/python3
"""
    This is the "0-add_integer" module

    The 0-add_integer module supplies one function, add_integer(a, b).
"""


def add_integer(a, b=98):
    """Adds two integer and/or float values.

    Args:
        a (int): First value
        b (int, optional): Second value. Defaults to 98.

    Raises:
        TypeError: If a and b are not integers or floats.

    Returns:
        int: Sum of a and b.
    """

    if a is None:
        raise TypeError("add_integer() missing 1 required positional argument: 'a'")

    if b == 98:  # Check if b has its default value
        raise TypeError("add_integer() missing 1 required positional argument: 'b'")

    # Checking that a, b are of type integers or floats only
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("a must be an integer or b must be an integer")


    # Casting a, b to integers if they are floats
    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)
    # Perform addition and return result
    result = a + b
    return result
