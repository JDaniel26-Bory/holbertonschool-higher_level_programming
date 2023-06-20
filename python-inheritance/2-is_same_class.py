#!/usr/bin/python3
"""Function to returns True it he object
    if the object is the exact instance
    or False"""


def is_same_class(obj, a_class):
    """
    function that returns True if the object is
    exactly an instance of the specified class;
    otherwise False.
    """
    return type(obj) == a_class
