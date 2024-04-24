#!/usr/bin/python3
""" Defines the Rectangle class that inherits from Base class. """
from models.base import Base


class Rectangle(Base):
    """ Representation of the Rectangle class. """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Intitializes a new Rectangle.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x coordinate of the rectangle.
            y (int): The y coordinate of the rectangle.
            id (int): The id of the new rectangle.

        Raises:
            TypeError: If width or height or x or y are not integers.
            ValueError: If width or height or x or y are less than 0.
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """ Set/get the width of the rectangle. """
            return self.__width

        @width.setter
        def width(self, value):
            if type(value) is not int:
                raise TypeError("width must be an integer.")

            if value <= 0:
                raise ValueError("width must be bigger than 0.")

            self.__width = value

        @property
        def height(self):
            """ Set/get the height of the rectangle. """
            return self.__height

        @height.setter
        def height(self, value):
            if type(value) is not int:
                raise TypeError("height must be an integer.")

            if value <= 0:
                raise ValueError("height must be bigger than 0.")

        @property
        def x(self):
            """ Set/get the x coordinate of the rectangle. """
            return self.__x

        @x.setter
        def x(self, value):
            if type(value) is not int:
                raise TypeError("x coordinate must be an integer.")

            if value <= 0:
                raise ValueError("x coordinate must be bigger than 0.")

        @property
        def y(self):
            """ Set/get the y coordinate of the rectangle. """
            return self.__y

        @y.setter
        def y(self, value):
            if type(value) is not int:
                raise TypeError("y coordinate must be an integer.")

            if value <= 0:
                raise ValueError("y coordinate must be bigger than 0.")
