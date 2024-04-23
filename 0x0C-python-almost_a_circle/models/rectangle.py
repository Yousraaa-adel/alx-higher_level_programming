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

        @property
        def height(self):
            """ Set/get the height of the rectangle. """
            return self.__height

        @property
        def x(self):
            """ Set/get the x coordinate of the rectangle. """
            return self.__x

        @property
        def y(self):
            """ Set/get the y coordinate of the rectangle. """
            return self.__y
