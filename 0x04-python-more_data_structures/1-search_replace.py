#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """function to search and replace an element

    Arguments:
        my_list: the given list
        search: the element to be searched
        replace: the replaced value

    Returns:
        a new matrix
    """
    if my_list is None:
        return
    new_list = my_list.copy()
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list
