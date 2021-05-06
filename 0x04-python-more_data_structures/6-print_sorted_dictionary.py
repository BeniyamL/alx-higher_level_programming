#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """function to sort a dictionary

    Arguments:
        a_dictionary: the given dictionary

    Returns:
        nothing
    """
    sorted_dict = sorted(a_dictionary.items())
    for k, v in sorted_dict:
        print("{0}: {1}".format(k, v))
