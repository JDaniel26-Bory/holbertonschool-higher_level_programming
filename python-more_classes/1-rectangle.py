#!/usr/bin/python3
"""Rectangle class
"""


class Rectangle:
    """Define a Rectangle class with width and height"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width value
        Returns:
            int: width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set width value

        Raises:
            TypeError: when value is not int
            ValueError: when value is a negative integer
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get height value

        Returns:
            int: height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set height value

        Raises:
            TypeError: when value is not int
            ValueError: when value is a negative integer
        """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
