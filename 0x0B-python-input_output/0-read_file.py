#!/usr/bin/python3
""" A Module contaiing a function called read_file """


def read_file(filename=""):
    """ Reads a file and prints to stdout

    Args:
        filename (str, optional): name of the file to read.
        Defaults to ""
    """
    with open(filename, 'r', encoding="utf-8") as file:
        content = file.read()
        print(content, end="")
