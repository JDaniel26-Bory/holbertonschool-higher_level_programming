#!/usr/bin/python3
"""BaseGeometry class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""Rectangle Class"""


class Rectangle(BaseGeometry):
    """width and height must be private.
        width and height must be positive integers
        validated by integer_validator
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
