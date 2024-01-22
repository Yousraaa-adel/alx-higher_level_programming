#!/usr/bin/python3
"""
    This is the "1-safe_print_integer" module

    The 1-safe_print_integer module supplies one function.
"""


def safe_print_integer(value):
    """Prints an integer with "{:d}".format().

    Args:
        value (any data type): the value to be printed

    Raises:
        ValueError and TypeError

    Returns:
        True: if an integer is printed
        False: otherwise
    """
    try:
        print("{:d}".format(value))
        print("")
        return True
    except (ValueError, TypeError):
        return False
