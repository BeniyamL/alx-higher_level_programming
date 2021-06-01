#!/usr/bin/python3
""" function defintion for append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """ function to write a text after search string

    Arguments:
        filename: the name of the file
        search_string: the text to be searched
        new_string: the string to be appended
    Returns:
        nothing
    """
    result_string = ""
    with open(filename) as file:
        for line in file:
            result_string += line
            if search_string in line:
                result_string += new_string
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(result_string)
