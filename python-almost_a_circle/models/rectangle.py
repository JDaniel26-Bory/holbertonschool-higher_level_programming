#!/usr/bin/python3
"""Rectangle Class"""


from models.base import Base


class Rectangle(Base):
    """Define Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialisation of Rectangle"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Width Getter"""
        return self.__width

    @property
    def height(self):
        """Height Getter"""
        return self.__height

    @property
    def x(self):
        """x Getter"""
        return self.__x

    @property
    def y(self):
        return self.__y

    width.setter

    """Set the value in private instance attribute"""
    def width(self, value):
        self.__width = value

    height.setter

    """Set the value in private instance attribute"""
    def height(self, value):
        self.__height = value

    x.setter

    def x(self, value):
        """Set the value in private instance attribute"""
        self.__x = value

    y.setter

    """Set the value in private instance attribute"""
    def y(self, value):
        self.__y = value
