#!/usr/bin/python3
def safe_print_integer(value):
    """function that prints an integer list

    Arguments:
        value: the value to be printed

    Returns:
        True if value is an integer False otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except:
            return False
