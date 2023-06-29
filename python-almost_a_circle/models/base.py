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

    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
