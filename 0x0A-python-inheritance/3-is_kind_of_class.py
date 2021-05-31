#!/usr/bin/python3
"""funciton definiton for is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """ check whether an object is an instance of the class that is inherited

    arguments:
        obj: the object to be checked
        a_class: the given class
    Returns:
        True if the object in instance of the specified classs False otherwise
    """
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
