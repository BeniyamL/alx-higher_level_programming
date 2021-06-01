#!/usr/bin/python3
""" function defintion for to_json_string
"""
import json


def to_json_string(my_obj):
    """ function to convert to JSON representation

    Arguments:
        my_obj: the given object
    Returns:
        JSON representatoin of an object
    """
    return json.dumps(my_obj)
