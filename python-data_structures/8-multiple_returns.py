#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence == 0:
        first_character = None
    else:
        first_character = sentence[0]
    return length, first_character
    