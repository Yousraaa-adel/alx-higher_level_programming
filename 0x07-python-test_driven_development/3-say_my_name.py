#!/usr/bin/python3
"""
    This is the "3-say_my_name" module

    The 3-say_my_name module divides all elements of a matrix.
"""
def say_my_name(first_name, last_name=""):
    """Prints my name.

    Args:
        first_name (str): First value
        last_name (str): Second value

    Raises:
        TypeError: If first_name or las_name are NOT of type str

    Returns:
        str: My name is <first name> <last name>
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    # Print the full name with last_name if provided, otherwise just first_name
    if last_name:
        print("My name is {} {}".format(first_name, las_name))
    else:
        print("My name is {}".format(first_name, las_name))
    
