#!/usr/bin/python3
""" Defines the base class for all other classes in this project. """
import json
import os


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

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file.

        Args:
            cls (class): The Base class.
            list_objs (list): list of instances who inherits of Base.
        """

        file_name = f"{cls.__name__}.json"

        if list_objs is None:
            list_objs = []

        # Convert list of objs to a list of dicts
        list_of_dicts = [obj.to_dictionary() for obj in list_objs]

        # Convert list of dicts to a JSON string
        json_string = cls.to_json_string(list_of_dicts)

        with open(file_name, "w") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string. """

        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes.

        Args:
            cls (class): The classes.
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(2, 5)
            elif cls.__name__ == "Square":
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances.

        cls (class): The classes.
        """

        file_name = str(cls.__name__) + ".json"
        try:
            with open(file_name, "r") as f:
                list_ds = Base.from_json_string(f.read())
                return [cls.create(**dic) for dic in list_ds]
        except IOError:
            return []
