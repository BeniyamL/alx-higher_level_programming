#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    print_reversed_list_integer - print an integr list
    @my_list: the given list
    @Return : the reversed list
    """
    if my_list is None:
        return
    for i in range(len(my_list) - 1, -1, -1):
        print("{0:d}".format(my_list[i]))
