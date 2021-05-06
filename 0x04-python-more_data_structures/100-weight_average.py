#!/usr/bin/python3
def weight_average(my_list=[]):
    """function that finds the weighted average of the list

    Arguments:
        my_list: the given list

    Returns:
        the weighted average
    """
    if my_list is None or len(my_list) == 0:
        return 0
    s = 0
    weight = 0
    for num in my_list:
        s += (num[0] * num[1])
        weight += num[1]
    return s / weight
