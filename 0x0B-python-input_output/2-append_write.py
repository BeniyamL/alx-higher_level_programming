#!/usr/bin/python3
""" function defintion for append_write
"""


def append_write(filename="", text=""):
    """ function to append a file

    Arguments:
        filename: the name of the file
        text: the text to be appended
    Returns:
        the number of characters wrotten
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
