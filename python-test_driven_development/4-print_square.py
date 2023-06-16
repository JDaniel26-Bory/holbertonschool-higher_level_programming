#!/usr/bin/python3
"""
Write a function that prints a square with the character #
"""


def print_square(size):
    """
    size is the size length of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise TypeError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
