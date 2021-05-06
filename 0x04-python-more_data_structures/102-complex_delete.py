#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """function that deletes a given element

    Arguments:
        a_dictionary: the given dictionary
        value: the given value

    Returns:
        the updated dictionary
    """
    while value in a_dictionary.values():
        for k, v in a_dictionary.items():
            if v == value:
                del a_dictionary[k]
                break
    return a_dictionary
