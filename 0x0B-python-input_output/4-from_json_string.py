#!/usr/bin/python3
""" A Module that has the function from_json_string """
import json


def from_json_string(my_str):
    """ returns an object represented by a JSON string
    Args:
        my_str (str): String to be decoded
    """
    return json.loads(my_str)
