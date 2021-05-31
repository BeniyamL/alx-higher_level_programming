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

    def area(self):
        """ function to find area of the rectanngle

        Arguments:
            nothing
        Returns:
            return the area of the rectangle
        """
        return (self.__width * self.__height)

    def __str__(self):
        """ function to print the rectangle information

        Arguments:
            nothing
        Returns:
            the string representation of a rectangle
        """
        rect_str = "[Rectangle] "
        rect_str += str(self.__width) + "/" + str(self.__height)
        return (rect_str)
