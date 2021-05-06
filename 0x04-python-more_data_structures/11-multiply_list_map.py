#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """function to multiply a list with a number

    Arguments:
        my_list: the given list
        number: the multipliere

    Returns:
        the new list
    """
    return list(map(lambda x: x * number, my_list))
