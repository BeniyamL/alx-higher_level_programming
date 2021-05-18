#!/usr/bin/python3
class Square:
    """ a square class to define atributes and methods of a square """

    def __init__(self, size=0, position=(0, 0)):
        """ function to initialize the square class

        Arguments:
           size: the size of the square
        Returns:
           nothing
        """

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ getter function of position

        Arguments:
           nothing
        Returns:
            the size of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ setter function to update the position of the square

        Arguments:
            value: the value we are going to set
        Returns:
            nothing
        """
        if type(value) is not tuple or len(value) != 2 or
        type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ function to find the area of the square

        Arguments:
            nothing
        Returns:
            the area of the square
        """

        return self.__size ** 2

    def my_print(self):
        """ function to print the character # to stdout

        Arguments:
            nothing
        Returns:
            nothing
        """
        if self.__size == 0:
            print()
            return
        for j in range(self.position[1]):
            print()
        for i in range(self.__size):
            for k in range(self.position[0]):
                print(" ", end="")
            print("#" * self.__size)
