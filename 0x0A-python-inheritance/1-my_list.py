#!/usr/bin/python3
"""
class definition of sub class Mylist
"""


class MyList(list):
    """
    the sub class MyList that is inherited from list
    """

    def print_sorted(self):
        """
        print_sorted- function to print the list in ascending order

        arguments:
            nothing
        Returns:
            list in sorted order
        """
        print(sorted(self))
