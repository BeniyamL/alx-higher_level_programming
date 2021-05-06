#!/usr/bin/python3
def uniq_add(my_list=[]):
    """function to add unique elements

    Arguments:
        my_list: the given list

    Returns:
        the sum of the list
    """
    sum = 0
    new_list = set(my_list)
    for n in new_list:
        sum += n
    return sum
