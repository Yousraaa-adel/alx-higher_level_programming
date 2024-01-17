#!/usr/bin/python3
""" A Module that has the Student Class """


class Student:
    """
    Class that defines properties of student.

    Attributes:
        first_name (str): first name of student
        last_name (str): last name of student
        age (int): age of the student
    """
    def __init__(self, first_name, last_name, age):
        """Creates new instances of Student.

        Args:
            first_name (str): first name of student
            last_name (str): last name of student
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of
        a Student instance

        Returns:
            dict: dictionary.
        """
        if attrs is None:
            return self.__dict__

        new_dict = []
        for item in attrs:
            try:
                new_dict[item] = self.__dict__[item]
            except Exception:
                pass

            return new_dict
