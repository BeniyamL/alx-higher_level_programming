#!/usr/bin/python3
def no_c(my_string):
    """
    no_c - remove all characters c and C from a string
    @my_string: the given string
    @Return : the new string
    """
    new_string = [c for c in my_string if c != 'c' and c != 'C']
    new_string = "".join(new_string)
    return new_string
