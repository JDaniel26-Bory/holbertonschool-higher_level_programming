#!/usr/bin/python3
""" Import class"""

Rectangle = __import__('9-rectangle').Rectangle

"""Square Class"""


class Square(Rectangle):
    """
    size must be private. No getter or setter
    size must be a positive integer, validated by integer_validator
    """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    """ should return, the square description: [Square] <width>/<height>"""
    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
