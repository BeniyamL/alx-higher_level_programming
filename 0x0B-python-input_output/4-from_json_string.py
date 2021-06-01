#!/usr/bin/python3
""" function defintion for to_json_string
"""
import json


def from_json_string(my_str):
    """function to convert JSON representation to python object

    Arguments:
        my_str: the json serialized string
    Returns:
        python represenation
    """
    return json.loads(my_str)
