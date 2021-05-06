#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """function to delete an element from a dictionary

    Arguments:
        a_dictionary: the given dictionary
        key: the key of the dictionary

    Returns:
        the updated dictionary
    """
    if key in a_dictionary.keys():
        del a_dictionary[key]
    return a_dictionary
