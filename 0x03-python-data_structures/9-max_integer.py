#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    max_integer - find the biggest number
    @my_list: the given list
    @Return : the biggest number
    """
    if my_list is None or len(my_list) == 0:
        return None
    max = my_list[0]
    for n in my_list:
        if n > max:
            max = n
    return max
