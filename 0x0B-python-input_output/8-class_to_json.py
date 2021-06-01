#!/usr/bin/python3
""" function defintion for class_to_json
"""


def class_to_json(obj):
    """ function to find dictionary representation of an object

    Arguments:
        obj: the given object
    Returns:
        dictionary representation of an object
    """
    return obj.__dict__
