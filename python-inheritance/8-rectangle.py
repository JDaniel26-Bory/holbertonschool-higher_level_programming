#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """Define class BaseGeometry
    """
    def area(self):
        """Define an exception for area method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validate argument value"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""Rectangle Class"""


class Rectangle(BaseGeometry):
    """width and height must be private.
        width and height must be positive integers
        validated by integer_validator
    """
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
