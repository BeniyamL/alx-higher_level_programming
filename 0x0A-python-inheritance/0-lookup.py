#!usr/bin/python3
"""
class definition lookup
"""


def lookup(obj):
    """
    lookup - function to find lsit of availabel attributes and methods

    arguments:
        obj: the given object
    Returns:
        list of available attributes and methods
    """
    return dir(obj)
