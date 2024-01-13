#!/usr/bin/python3
"""
    This is the "4-print_square" module

    The 4-print_square module divides all elements of a matrix.
"""
def print_square(size):
    """ Prints a square with the character #.

    Args:
        size (int): Size of the square's side length.

    Raises:
        TypeError: If size is NOT of type int
        TypeError: If size is a float and is less than 0
        ValueError: If size is less than 0

    Returns:
        str: prints a square with the character #.
    
    Example:
        >>> print_square(3)
        ###
        ###
        ###
    """

    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for row in range(size):
        print("#", end="")
        for col in range(1, size):
            print("#", end="")
        print("")
