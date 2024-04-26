#!/usr/bin/python3
""" Defines a Square class that inherits from Rectangle class. """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Representation of the Square class. """

    def __init__(self, size, x=0, y=0, id=None):
        """ Intizializes a new square.

        Args:
            size (int): The size of the new square.
            x (int): The x cordinate of the new square. Default is 0.
            y (int): The y coordinate of the new square. Default is 0.
            id (int): the identity of the new square. Default is None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Return a string representation of the square. """

        return f"[Square] ({self.id}) {self.x}/{self.y} - " \
            f"{self.width}"
