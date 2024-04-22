#!/usr/bin/python3
""" Defines a class MyList that inherits from list """


class MyList(list):
    """
        Returns a new list sorted in an ascending order
    """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted(sorted_list))
