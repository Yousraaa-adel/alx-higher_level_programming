#!/usr/bin/python3
""" Defines the base class for all other classes in this project. """
import json


class Base():
    """ Represents the Base class. """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Intitializes the class.

        Args:
            id (int): The id of the new base. Defaults to None.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries. """

        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
