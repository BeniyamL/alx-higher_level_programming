#!usr/bin/python3
"""
class definition MyInt
"""


class MyInt(int):
    """
    class for my int
    """
    def __eq__(self, val):
        """ function to invert equality

        arguments:
            val: the given value
        Returns:
            True if is not equal
        """
        return (self.real != val)

    def __ne__(self, val):
        """ function to invert not equal

        Arguments:
            val: the given value
        Returns:
           True if it is equal
        """
        return (self.real == val)
