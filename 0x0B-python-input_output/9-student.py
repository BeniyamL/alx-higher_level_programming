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
            obj: the given object
        Returns:
            dictionary representation of an object
        """
        return self.__dict__
