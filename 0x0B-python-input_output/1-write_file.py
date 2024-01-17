#!/usr/bin/python3
""" A Module that contains the function write_file """


def write_file(filename="", text=""):
    """ writes a string to a text file and returns the number
        of characters written

    Args:
        filename (str): the file that will be writing in
        text (str): text to be appended
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        count = len(text)
        return count
