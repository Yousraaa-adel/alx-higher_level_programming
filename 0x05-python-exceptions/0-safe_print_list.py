#!/usr/bin/python3
"""
    This is the "0-safe_print_list" module

    The 0-safe_print_list module supplies one function.
"""


def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list.

    Args:
        my_list (list): the list with items to be printed
        x (int): num of items to be printed from my_list. Defaults to 0.

    Raises:
        IndexError: when x is bigger than my_list
    """
    count = 0

    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            break

    print()
    return count


if __name__ == "__main__":
    main()
