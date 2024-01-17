#!/usr/bin/python3
""" A Module that has the function to_json_string """
import json


def to_json_string(my_obj):
    """ returns the JSON representation of an object (string)

    Args:
        my_obj ():
    """
    return json.dumps(my_obj)
