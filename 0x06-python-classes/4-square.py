##!/usr/bin/python3
class Square:
    """ a square class to define atributes and methods of a square """

    def __init__(self, size=0):
        """ function to initialize the square class

        Arguments:
           size: the size of the square
        Returns:
           nothing
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """ getter function of size

        Arguments:
           nothing
        Returns:
            the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter function to update the size of the square

        Arguments:
            value: the value we are going to set
        Returns:
            nothing
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ function to find the area of the square

        Arguments:
            nothing
        Returns:
            the area of the square
        """
        return self.__size ** 2
