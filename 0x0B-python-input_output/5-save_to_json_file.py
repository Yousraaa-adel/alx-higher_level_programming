#!/usr/bin/python3
""" A Module that has the function save_to_json_file """
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation:

    Args:
        my_obj: Object to be written in a file
        filename: File that will write in
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
