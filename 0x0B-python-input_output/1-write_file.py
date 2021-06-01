#!/usr/bin/python3
""" function defintion for write_file
"""


def write_file(filename="", text=""):
    """ function to write a file

    Arguments:
        filename: the name of the file
        text: the text to be written
    Returns:
        the number of characters wrotten
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
