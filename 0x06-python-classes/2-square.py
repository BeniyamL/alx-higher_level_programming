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
