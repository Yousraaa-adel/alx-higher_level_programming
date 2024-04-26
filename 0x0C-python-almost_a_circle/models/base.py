#!/usr/bin/python3
""" Defines the base class for all other classes in this project. """


class Base():
    """ Represents the Base class. """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Intitializes the class.

        Args:
            id (id): The id of the new base. Defaults to None.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
