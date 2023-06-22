#!/usr/bin/python3
"""Function that reads a text file
    and prints it in the stdout
"""


def read_file(filename=""):
    """Print file only read"""
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
