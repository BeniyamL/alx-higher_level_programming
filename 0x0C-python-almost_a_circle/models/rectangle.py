#!/usr/bin/python3
""" Rectangle class definition """
from models.base import Base


class Rectangle(Base):
    """ a rectangle class to define atributes and methods of a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ function to initialize the rectangel class

        Arguments:
           width: the width of the rectangle
           height: the height of the rectangle
           x: x point of the rectangle
           y: y point of the recangle
           id: the id of the module
        Returns:
           nothing
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter function of width

        Arguments:
            nothing
        Returns:
            the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, width):
        """ setter function of width

        Arguments:
            width: the width of the rectangle
        Returns:
            nothing
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ getter function of height

        Arguments:
            nothing
        Returns:
            the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, height):
        """ setter function of height

        Arguments:
            height: the height of the rectangle
        Returns:
            nothing
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ getter function of x

        Arguments:
            nothing
        Returns:
            the x of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, x):
        """ setter function of x

        Arguments:
            x: the width of the rectangle
        Returns:
            nothing
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ getter function of y

        Arguments:
            nothing
        Returns:
            the y of the rectangle
        """
        return self.__y

    @y.setter
    def y(self, y):
        """ setter function of y

        Arguments:
            y: the y of the rectangle
        Returns:
            nothing
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ function to find area of a rectangle

        Arguments:
            nothing
        Returns:
            the area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """ function to display a rectangle

        Arguments:
            nothing
        Returns:
            nothing
        """
        if self.width == 0 or self.height == 0:
            print("")
            return
        for k in range(self.y):
            print()
        for i in range(self.height):
            for m in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """ string representation of the class rectangle

        Arguments:
            nothing
        Returns:
            nothing
        """
        rct_str = "[Rectangle] " + "(" + str(self.id) + ") " + str(self.x)
        rct_str += "/" + str(self.y) + " - " + str(self.width)
        rct_str += "/" + str(self.height)
        return rct_str

    def update(self, *args, **kwargs):
        """ function to update rectangle's attributes

        Arguments:
           args: set of arguments decscribed below
                - 1st argument: id
                -2nd argument: width
                -3rd argument: height
                -4th argument: x
                -5th argument: y
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
                    self.width = arg
                elif index == 2:
                    self.height = arg
                elif index == 3:
                    self.x = arg
                elif index == 4:
                    self.y = arg
                index += 1
        elif kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is not None:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ dictionary representation of a rectangle class

        Arguments:
            nothing
        Returns:
            dictionary representation of a rectangle class
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
