#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """
    Class that defines properties of rectangle by: (based on 0-rectangle.py).

    Attributes:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """Creates new instances of Rectangle.

        Args:
            width (int, optional): width of rectangle. Defaults to 0.
            height (int, optional): height of rectangle. Defaults to 0.
        """
        self.__height = height
        self.__width = width
    
    @property
    def width(self):
        """Width retriver.

        Returns:
            int: the width of the rectangle.
        """
        return self.__width
    
    @property
    def height(self):
        """Height retriver.

        Returns:
            int: the height of the rectangle.
        """
        return self.__height
    
    @width.setter
    def width(self, value):
        """Property setter for width of rectangle.

        Args:
            value (int): width of the rectangle.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Property setter for height of recyangle.

        Args:
            value (int): height of the rectangle.

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates area of Rectangle

        Returns:
            int: area of Rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates perimeter of Rectangle

        Returns:
            int: perimeter of Rectangle
        """
        if (self.__width == 0) or (self.__height == 0):
            return 0
        else:
            return 2 * (self.__width + self.__height)
    
    def __str__(self):
        """Prints the rectangle with the character #.

        Returns:
            str: the rectangle
        """
        rectangle = []

        # Checking if either is zero then abort
        if (self.__width == 0) or (self.__height == 0):
            return ""
        
        # Looping over both height and then width to print #
        for h in range(self.__height):
            for w in range(self.__width):
                rectangle.append("#")
            rectangle.append("\n")
        
        # Removes the last empty line
        rectangle.pop()

        return "".join(rectangle)

    def __repr__(self):
        """Returns a string representation of the rectangle.

        Returns:
            str: the rectangle representation.
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes an instance of a class
        """
        print("{:s}").format("Bye rectangle...")
