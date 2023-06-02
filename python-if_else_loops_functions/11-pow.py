#!/usr/bin/python3
def pow(a, b):
    power = 1
    for i in range(1, b + 1):
        power *= a
    return power
