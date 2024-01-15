#!/usr/bin/python3

""" This class initiates a new Rectangle class 
    with property and setter for both: width and height.
    

    The new line at the end of the file is a project requirement.

"""


class Rectangle:
    """ Represents a Rectangle
    
    Args:
        height: the height of the new Rectangle
        width: the width of the new Rectangle
    
    Raises:
        TypeError: If width is not an integer
        TypeError: If height is not an integer
        ValueError: If width is less than 0
        ValueError: If height is less than 0
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(width, int) or isinstance(width, bool):
            raise TypeError("width must be an integer")
        
        if width < 0:
            raise ValueError("width must be >= 0")


    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(height, int) or isinstance(height, bool):
            raise TypeError("height must be an integer")
        
        if height < 0:
            raise ValueError("height must be >= 0")
