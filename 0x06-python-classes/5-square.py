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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns the current area of the Square. """
        return (self.__size * self.__size)

    def my_print(self):
        """  prints in stdout the square with the character # """

        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
