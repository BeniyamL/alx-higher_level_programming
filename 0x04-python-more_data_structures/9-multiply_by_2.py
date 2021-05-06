#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """function that multiply all values of a dictionary by 2

    Arguments:
        a_dictionary: the given dictionary

    Returns:
        the new dictionary
    """
    new_dict = a_dictionary.copy()
    for k, v in a_dictionary.items():
        new_dict[k] = v * 2
    return new_dict
