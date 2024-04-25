#!/usr/bin/python3
""" Defines a Square class that inherits from Rectangle class. """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Representation of the Square class. """

    def __init__(self, size, x=0, y=0, id=None):
        """ Intizializes a new square.

        Args:
            size (int): The size of the new square.
            x (int): The x cordinate of the new square.
            y (int): The y coordinate of the new square.
            id (int): the identity of the new square.
        """
        super().__init__(size, size, x=0, y=0, id)

    def __str__(self):
        """ Override the __str__ method. """

        return f"[Square] ({self.id}) {self.x}/{self.y} - " \
            f"{self.width}/{self.height}"
