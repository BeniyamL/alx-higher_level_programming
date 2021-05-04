#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    new_in_list - replace an element of a list in a copy
    @my_list: the given list
    @idx: the given index
    @element: element to be replaced
    @Return : the replaced element
    """

    new_list = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        new_list[idx] = element
        return new_list
