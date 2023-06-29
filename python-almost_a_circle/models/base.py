#!/usr/bin/python3
"""Define Base Class"""

import json
import csv


class Base:
    """Define Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialisation, integer identification. Defaults to None.
        """

        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Function to returns the JSON string
        representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of list_objs to a file"""
        list_cls = []
        if list_objs is not None:
            for i in list_objs:
                list_cls += [(cls.to_dictionary(i))]

        with open(cls.__name__ + ".json", "w", encoding="utf-8") as w:
            w.write(cls.to_json_string(list_cls))

    @staticmethod
    def from_json_string(json_string):
        """Function that returns the list of
        the JSON string representation"""
        if json_string == '[]' or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Function with instance
        with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        if cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Function that load the objcets of a CSV file
        as dictionary, create instances and returns a
        list of instances"""
        filename = cls.__name__ + '.json'
        try:
            with open(filename, "r") as file:
                json_str = file.read()
                dictionaries = cls.from_json_string(json_str)
                return [cls.create(**dictionary)
                        for dictionary in dictionaries]
        except FileNotFoundError:
            return []
