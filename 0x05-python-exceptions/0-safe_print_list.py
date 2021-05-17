#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """function that prints a list

    Arguments:
        my_list: the given list
        x: the number of elements to be printed

    Returns:
        the real number of elements printed
    """
    num = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            num = num + 1
        except IndexError:
            break
    print()
    return num
