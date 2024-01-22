#!/usr/bin/python3
"""
    This is the "3-safe_print_division" module

    The 3-safe_print_division module supplies one function.
"""


def safe_print_division(a, b):
    """Divides 2 integers and prints the result.

    Args:
        a (int): first value
        b (int): second value

    Raises:
        ValueError and TypeError
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))

    return result
