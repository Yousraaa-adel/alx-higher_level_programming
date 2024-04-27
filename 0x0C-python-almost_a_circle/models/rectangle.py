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
            ValueError: If width or height are < 0.
            ValueError: If x or y are <= 0.
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Width getter. """
        return self.__width

    @width.setter
    def width(self, value):
        """ Width setter. """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ Height getter. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height setter. """
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """ X getter. """
        return self.__x

    @x.setter
    def x(self, value):
        """ X setter. """
        if type(value) is not int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """ Y getter. """
        return self.__y

    @y.setter
    def y(self, value):
        """ Y setter. """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """ Calculates the area of the rectangle. """
        return self.width * self.height

    def display(self):
        """ Prints Rectangle in stdout using #. """
        for y in range(self.y):
            print("")
        for r in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for col in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """ Overrides the __str__method. """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - " \
            f"{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute.

        Args (ints):
            1st argument represents be the id attribute.
            2nd argument represents be the width attribute.
            3rd argument represents be the height attribute.
            4th argument represents be the x attribute.
            5th argument represents be the y attribute.

        Kwargs (dict): Pairs of keys/values (keyworded args).
        """
        if args:
            for i in range(len(args)):
                if i == 0:
                    if args[i] is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle. """

        dict1 = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

        return dict1
