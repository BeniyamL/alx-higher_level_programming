#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """ executes the function safely

    Arguments:
        args: an array of arguments

    Returns:
        the result of the funciton
    """
    try:
        result = fct(*args)
    except:
        result = None
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
    return result
