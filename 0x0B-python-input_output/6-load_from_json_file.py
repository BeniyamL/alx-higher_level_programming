#!/usr/bin/python3
""" function defintion for load_from_json_file
"""
import json


def load_from_json_file(filename):
    """ function to create an object from JSON

    Arguments:
        filename: the name of the file
    Returns:
        the created python object
    """
    with open(filename) as file:
        return json.load(file)
