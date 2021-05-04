#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """print an integr list

    Args:
        my_list: the given list

    Returns:
        nothing
    """
    for n in my_list:
        print("{0:d}".format(n))
