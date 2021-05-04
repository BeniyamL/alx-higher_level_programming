#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    add_tuple - add two tuple
    @tuple_a: the first tuple
    @tuple_b: the second tuple
    @Return : the tuple with 2 integers
    """
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    tuple_add = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return tuple_add
