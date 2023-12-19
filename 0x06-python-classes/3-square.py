#!/usr/bin/python3

""" Define a class Square """


class Square:
    """ Represent a class Square """
    def __init__(self, self=0):
        """ Initializes a Square instance.

        Args:
            size (int): The size of the square. Defualts to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(self, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Returns the current area of the square """

        return (self.__size * self.__size)
