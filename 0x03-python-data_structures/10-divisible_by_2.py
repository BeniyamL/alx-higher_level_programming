#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    divisible_by_2 - find mulitples of 2 in a list
    @my_list: the given list
    @Return : a list for multiples of 2
    """
    if my_list is None or len(my_list) == 0:
        return my_list
    multiple_of_2 = my_list.copy()
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiple_of_2[i] = True
        else:
            multiple_of_2[i] = False
    return multiple_of_2
