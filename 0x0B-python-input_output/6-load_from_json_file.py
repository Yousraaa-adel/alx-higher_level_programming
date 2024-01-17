#!/usr/bin/python3
""" A Module that has the function load_from_json_file """
import json


def load_from_json_file(filename):
    """ creates an Object from a “JSON file”

    Args:
        filename: File that an obj will be created from
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
