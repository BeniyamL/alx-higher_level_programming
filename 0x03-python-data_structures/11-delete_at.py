#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    delete_at - delete element at a given index
    @my_list: the given list
    @idx: the given index
    @Return : the new list
    """

    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
