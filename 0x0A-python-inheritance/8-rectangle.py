#!/usr/bin/python3
""" Defines a class called Rectangle to inherit from BaseGeometry. """


BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    """ Represents a Rectangle using BaseGeometry. """

    def __init__(self, width, height):
        """ Intializes a new Rectangle.

        Args:
            width (int): The width of a new Rectangle.
            height (int): The height of a new Rectangle.
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
