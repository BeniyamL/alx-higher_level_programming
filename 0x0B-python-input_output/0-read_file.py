#!/usr/bin/python3
""" function defintion for read_file
"""


def read_file(filename=""):
    """ function to read a file

    Arguments:
        filename: the name of the file to be read
    Returns:
        nothing
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
