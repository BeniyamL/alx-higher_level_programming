#!/usr/bin/python3
""" class defintion for Rectangle
"""


class Rectangle:
    """ Rectangel class """

    @property
    def width(self):
        """ getter method of width

        Arguments:
            nothing
        Returns:
            the width of the rectangel
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter method for the width

        Arguments:
            the width value
        Returns:
            nothing
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter method for height

        Arguments:
            nothing
        Returns:
            the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter metod for height

        Arguments:
            the height value
        Returns:
            nothing
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        """ initialize the widht and height of the rectangel

        Arguments:
            width: the width of the rectangle
            height: the height of the rectangle
        Returns:
            nothing
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    def area(self):
        """ function to find the area of the rectangle

        Arguments:
            nothing
        Returns:
            the area of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """ fucntion to find perimeter of the ractangle

        Arguments:
            nothing
        Returns:
            the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))
