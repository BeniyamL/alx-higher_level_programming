#!/usr/bin/python3
""" Square class definition """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ a square class to define atributes and methods of a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """ function to initialize the square class

        Arguments:
           size: the size of the square
           x: x point of the square
           y: y point of the square
           id: the id of the module
        Returns:
           nothing
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ getter function of size

        Arguments:
            nothing
        Returns:
            the size of the square
        """
        return self.width

    @size.setter
    def size(self, size):
        """ setter function of size

        Arguments:
            size: the size of the square
        Returns:
            nothing
        """
        self.width = size
        self.height = size

    def __str__(self):
        """ string representation of the class square

        Arguments:
            nothing
        Returns:
            nothing
        """
        sqr_str = "[Square] " + "(" + str(self.id) + ") " + str(self.x)
        sqr_str += "/" + str(self.y) + " - " + str(self.width)
        return sqr_str

    def update(self, *args, **kwargs):
        """ function to update Square's attributes

        Arguments:
           args: set of arguments decscribed below
                - 1st argument: id
                -2nd argument: size
                -3th argument: x
                -4th argument: y
          kwargs: set of paired key/value attributes
        Returns:
            nothing
        """
        if args is not None and len(args) != 0:
            index = 0
            for arg in args:
                if index == 0:
                    if arg is not None:
                        self.id = arg
                elif index == 1:
                    self.size = arg
                elif index == 2:
                    self.x = arg
                elif index == 3:
                    self.y = arg
                index += 1
        elif kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is not None:
                        self.id = value
                elif key == "size":
                    self.width = value
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ dictionary representation of a square

        Arguments:
            nothing
        Returns:
            dictionary representation of a square
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
