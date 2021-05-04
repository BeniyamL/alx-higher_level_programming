#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    replace_in_list - replace an element of a list
    @my_list: the given list
    @idx: the given index
    @element: element to be replaced
    @Return : the replaced element
    """

    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
