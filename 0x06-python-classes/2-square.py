#!/usr/bin/python3

""" Define a class Square """


class Square:
    """ Represent a Square """

    def __init__(self, size=0):
        """ Initializes a Square class.

        Args:
            size: The size of the square. Deafults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
