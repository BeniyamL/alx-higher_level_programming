#!/usr/bin/python3
"""
class definition of Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class implementation for rectangle
    """
    def __init__(self, width, height):
        """initialization of rectangle class

        Arguments:
            width: the width of the rectangle
            height: the height of the rectangle
        Returns:
            nothing
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
