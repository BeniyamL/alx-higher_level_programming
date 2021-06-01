#!/usr/bin/python3
""" class defintion Student
"""


class Student:
    """ implementation of class student """

    def __init__(self, first_name, last_name, age):
        """ initialization fuction of student

        Arguments:
            first_name: the first name of the student
            last_name: the last name of the student
            age: the age of the student
        Returns:
            nothing
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ function to find dictionary representation of an object

        Arguments:
            nothing
        Returns:
            dictionary representation of an object
        """
        return self.__dict__

    def to_json(self, attrs=None):
        """ function to find dictionary representation of an object

        Arguments:
            attrs: the given object attribute
        Returns:
            dictionary representation of an object
        """
        attrs_dict = {}
        if type(attrs) is list:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
                if attr in self.__dict__.keys():
                    attrs_dict[attr] = self.__dict__[attr]
            return attrs_dict
        return self.__dict__
