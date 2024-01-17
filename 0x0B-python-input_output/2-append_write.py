#!/usr/bin/python3
""" A Module that has the function append_write """


def append_write(filename="", text=""):
    """ appends a string at the end of a text file and returns
        the number of characters added

    Args:
        filename (str): the file in which we append the text
        text (str): text to be appeneded
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
