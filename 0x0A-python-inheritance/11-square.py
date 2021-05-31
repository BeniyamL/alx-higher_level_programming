#!usr/bin/python3
"""
class definition of square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class implementation for square
    """
    def __init__(self, size):
        """initialization of square class

        Arguments:
            size: the size of the square
        Returns:
            nothing
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ function to print the rectangle information

        Arguments:
            nothing
        Returns:
            the string representation of a rectangle
        """
        square_str = "[Square] " 
        square_str += str(self.__size) + "/" + str(self.__size)
        return (square_str)
