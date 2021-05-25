#!/usr/bin/python3
""" class definition for locked class
"""


class LockedClass:
    """ class to preven dynamically creating of new instance """

    __slots__ = 'first_name'
