#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """function that prints an integer value

    Arguments:
        value: the value to be printed

    Returns:
        True if value is an integer False otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except TypeError as Te:
        sys.stderr.write("Exception: " + str(Te) + "\n")
        return False
    except ValueError as Ve:
        sys.stderr.write("Exception: " + str(Ve) + "\n")
        return False
