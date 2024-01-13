#!/usr/bin/python3
"""
    This is the "4-print_square" module

    The 5-text_indentation divides all elements of a matrix.
"""
def text_indentation(text):
    """ Prints a square with the character #.

    Args:
        size (int): Size of the square's side length.

    Raises:
        TypeError: If size is NOT of type int
        TypeError: If size is a float and is less than 0
        ValueError: If size is less than 0

    Returns:
        str: prints a square with the character #.
    """

    if not isinstance(text, str) or isinstance(text, bool):
        raise TypeError("text must be a string")
    
    text = text.strip()
    newText = ""

    for c in text:
        if c in ['.', '?', ':']:
            newText += c + "\n\n"
        else:
            newText += c
        
    print(newText)
