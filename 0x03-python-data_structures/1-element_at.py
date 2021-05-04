#!/usr/bin/python3
def element_at(my_list, idx):
    """
    element_at - find element at an index
    @my_list: the given list
    @idx: the given index
    @Return : element at idx
    """

    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]
