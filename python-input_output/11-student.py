#!/usr/bin/python3
"""class Student"""


class Student():
    """Define class Student
    """
    def __init__(self, first_name, last_name, age):
        """Initialisation of public instance attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method to retrieve a dictionary representation
            of a student instance
        """
        if attrs is not None:
            dict_student = {}
            for i in self.__dict__:
                if i in attrs:
                    dict_student[i] = self.__dict__[i]
            return dict_student
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        """
        if json:
            self.__dict__ = json
