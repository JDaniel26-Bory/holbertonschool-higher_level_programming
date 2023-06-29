#!/usr/bin/python3
"""Define Base Class"""

import json


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
