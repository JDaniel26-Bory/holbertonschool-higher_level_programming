#!/usr/bin/python3
"""Rectangle Class"""


from models.base import Base


class Rectangle(Base):
    """Define Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialisation of Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
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

    @width.setter
    def width(self, value):
        """Set the value in private instance attribute"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the value in private instance attribute"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Set the value in private instance attribute"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Set the value in private instance attribute"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Define area class and returns the area value"""
        return self.__height * self.__width

    def display(self):
        """Define display class that prints in stdout"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Define str class"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
                (self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Define update class, that assigns an argument to each attribute"""
        attr = ['id', 'width', 'height', 'x', 'y']
        if args and args[0] is not None:
            for idx in range(len(args)):
                setattr(self, attr[idx], args[idx])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)
