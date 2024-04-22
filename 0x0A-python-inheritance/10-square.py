#!/usr/bin/python3
""" Defines Square class that inherits from Rectangle. """
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """ Represents the Square class. """

    def __init__(self, size):
        """ Creates an instance of the Square class.
        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
