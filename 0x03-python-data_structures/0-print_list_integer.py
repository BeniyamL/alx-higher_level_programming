#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    print_list_integer - print an integr list
    @my_list: the given list
    @Return : nothing
    """
    for i in range(len(my_list)):
        print("{0:d}".format(my_list[i]))
