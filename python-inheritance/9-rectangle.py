#!/usr/bin/python3
""" Import class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('8-rectangle').Rectangle

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

    """the area() method must be implemented"""
    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
