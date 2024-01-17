#!/usr/bin/python3
""" A Module that has the function class_to_json """


def class_to_json(obj):
    """ returns the dictionary description with simple
        data structure (list, dictionary, string,
        integer and boolean) for JSON serialization of an object:

    Args:
        obj: Object to be serialized

    Returns:
        dict: dictionary.
    """
    return obj.__dict__
