#!/usr/bin/python3
""" create functions"""


def add_integer(a, b=98):
    """funtion for adding integer"""
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")

    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
