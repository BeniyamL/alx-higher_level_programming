#!/usr/bin/python3
""" say_my_name function """


def say_my_name(first_name, last_name=""):
    """ function to print the first and last name

    Arguments:
        first_name: the first name
        last_name: the second name
    Returns:
        nothing
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
