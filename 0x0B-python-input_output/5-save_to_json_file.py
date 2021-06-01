#!/usr/bin/python3
""" function defintion for save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """ function that writes an object to a text file using JSON

    Arguments:
        filename: the name of the file
        my_obj: the python object to be saved
    Returns:
        nothing
    """
    with open(filename, mode="w") as file:
        json.dump(my_obj, file)
