#!/usr/bin/python3
""" Defines a Square class that inherits from Rectangle class. """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Representation of the Square class. """

    def __init__(self, size, x=0, y=0, id=None):
        """ Intizializes a new square. """
        super().__init__(size, size, x=0, y=0, id=None)

    def __str__(self):
        """ Override the __str__ method. """
        return f"[Square] ({self.id}) {self.x}/{self.y} - " \
            f"{self.width}/{self.height}"
