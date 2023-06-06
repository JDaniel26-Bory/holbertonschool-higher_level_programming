#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    if sentence == 0:
        first_character = None
    else:
        first_character = sentence[0]
    return l, first_character
