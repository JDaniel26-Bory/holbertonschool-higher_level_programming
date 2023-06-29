#!/usr/bin/python3
"""Square Class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Define Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Size Getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the value in private instance attribute"""
        self.width = value
        self.height = value

    def __str__(self):
        """String representation of a Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Define update class, that assigns an argument to each attribute"""
        attr = ['id', 'size', 'x', 'y']
        if args and args[0] is not None:
            for idx in range(len(args)):
                setattr(self, attr[idx], args[idx])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """dictionary representation of a Square"""
        new_dict = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return new_dict
