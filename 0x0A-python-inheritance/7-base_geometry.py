#!/usr/bin/python3
""" Defines an empty class called BaseGeometry. """


class BaseGeometry():
    """ Represents base BaseGeometry. """

    def area(self):
        """ Raises an Exception with the message area() is not implemented. """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value.
        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
