#!/usr/bin/python3
"""
    This is the "2-safe_print_list_integers" module

    The 2-safe_print_list_integers module supplies one function.
"""


def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list and only integers.

    Args:
        my_list (list): the list with items to be printed
        x (int): num of items to be printed from my_list. Defaults to 0.

    Raises:
        ValueError and TypeError

    Returns:
        The real number of integers printed
    """
    count = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]))
            count += 1
        except (ValueError, TypeError):
            pass
        except IndexError:
            break

    return count
