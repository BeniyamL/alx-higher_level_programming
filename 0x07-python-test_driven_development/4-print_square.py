#!/usr/bin/python3
""" print_square function """


def print_square(size):
    """ function to print a square of a given size

    Arguments:
        size: the size of the square
    Returns:
        nothing
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is int and size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
