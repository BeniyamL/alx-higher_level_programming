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


