#!/usr/bin/python3
""" definition of inherits_from """


def inherits_from(obj, a_class):
    """ check whether an object is an instance of inherited class

    arguments:
        obj: the object to be checked
        a_class: the given class
    Returns:
        True if it is an instance of inherited  classs False otherwise
    """
    if isinstance(obj, a_class) and
    issubclass(a_class, obj.__class__) is False:
        return (True)
    else:
        return (False)
