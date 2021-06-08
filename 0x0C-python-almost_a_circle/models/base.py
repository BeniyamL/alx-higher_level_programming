#!/usr/bin/python3
""" Base class definition """
import json
import csv


class Base:
    """ a base class to define atributes and methods of a base figure"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ function to initialize the base class

        Arguments:
           id: the id of the Base class
        Returns:
           nothing
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ function to convert to JSON string representation

        Arguments:
            dictionary object
        Returns:
            json representation of the dictionary
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ function to wirte the json string to a file

        Arguments:
            cls: the given class
            list_objs: the list object
        Returns:
            nothing
        """
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """ function to convert json string to python object

        Arguments:
            json_string: the given json string
        Returns:
            the python object of
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ function that returns an instance with all attributes

        Arguments:
            dictionary : dictionary represenation of an object
        Returns:
            an object with all attributes
        """
        if dictionary is not None and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_obj = cls(1, 1)
            else:
                new_obj = cls(1)
            new_obj.update(**dictionary)
            return new_obj

    @classmethod
    def load_from_file(cls):
        """ function that returns a lsit of instances

        Arguments:
            cls: the given object
        Returns:
            list of instances
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename) as jsonfile:
                list_dict = Base.from_json_string(jsonfile.read())
                return [cls.create(**dictionary) for dictionary in list_dict]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ function to save to csv

        Arguments:
            cls: the class
            list_objs: list objects
        Returns:
            nothing
        """
        filename = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            col_names = ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            col_names = ["id", "size", "x", "y"]
        with open(filename, mode="w", newline="") as csvfile:
            if list_objs is None or len(list_objs) == 0:
                csvfile.write("[]")
            else:
                blankfile = csv.DictWriter(csvfile, fieldnames=col_names)
                for obj in list_objs:
                    blankfile.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ function to load csv files

        Arguments:
            cls: the class
        Returns:
            nothing
        """
        filename = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            col_names = ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            col_names = ["id", "size", "x", "y"]
        try:
            with open(filename, mode="r", newline="") as csvfile:
                l_dict = csv.DictReader(csvfile, fieldnames=col_names)
                l_dict = [dict([key, int(value)] for key, value in d.items())
                          for d in l_dict]
                return [cls.create(**obj) for obj in l_dict]
        except IOError:
            return []
