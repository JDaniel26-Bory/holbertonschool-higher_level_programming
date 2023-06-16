#!/usr/bin/python3
"""Function that prints a text with two lines
    after enconters the characteres '.' '?' and ':'.
    The text must be a string and the lines printed
    should have extra spaces
"""


def text_indentation(text):
    """Print text with two newlines after ? . and : characters.
        Rise TypeError when text is not a str
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    punctuation_marks = ['.', '?', ':']
    for delim in punctuation_marks:
        text = delim.join([line.strip(" ") for line in text.split(delim)])
        text = text.replace(delim, delim + "\n\n")

    print(text, end="")
