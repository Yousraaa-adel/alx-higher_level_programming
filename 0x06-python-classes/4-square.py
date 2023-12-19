#!/usr/bin/python3

""" Define a Square class. """


class Square:
    """ Represent a Square class. """

    def __init__(self, size=0):
        """ Initializes a Square instance.

        Args:
            size (int): The size of the new square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """ Get/set the current size of the square """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("Size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns the current area of the Square. """
        return (self.__size * self.__size)

