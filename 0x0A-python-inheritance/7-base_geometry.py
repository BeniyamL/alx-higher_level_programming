#!usr/bin/python3
"""
class definition BaseGeometry
"""


class BaseGeometry:
    """
    empty class for gemometry
    """
    def area(self):
        """ function to find area

        arguments:
            nothing
        Returns:
            nothing
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ function to validate a value

        Arguments:
            name: the name of the geometry
            value: the value to be validated
        Returns:
            nothing
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
