#!/usr/bin/python3
import json
"""function that returns the JSON representation of an object (string)"""


def to_json_string(my_obj):
    """Output json object as a string"""
    return json.dumps(my_obj)
