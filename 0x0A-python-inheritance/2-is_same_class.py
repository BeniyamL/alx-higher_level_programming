#!usr/bin/python3
def is_same_class(obj, a_class):
    """
    is_same_class- check whether a class is an instance of the class

    arguments:
        obj: the object to be checked
        a_class: the given class
    Returns:
        True if the object in instance of the specified classs False otherwise
    """
    if type(obj) == a_class:
        return (True)
    else:
        return (False)
