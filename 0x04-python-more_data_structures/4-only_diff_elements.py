#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """function to find elements only in one of the set

    Arguments:
        set_1: the first list
        set_2: the second list

    Returns:
        the common element
    """
    return set_1 ^ set_2
