#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if len(sentence) < 0:
        return None
    else:
        first_character = sentence[0]
    return length, first_character
