#!/usr/bin/python3
"""Write a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """returns the number of characters written"""
    with open(filename, 'w', encoding="utf-8") as f:
        num_characters = f.write(text)
        return num_characters
