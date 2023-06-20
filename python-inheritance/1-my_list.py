#!/usr/bin/python3
""" Class Mylist that inherits
    from list
"""


class MyList(list):
    """Define Myclass subclass"""

    def print_sorted(self):
        """Prints the list sorted
        """
        print(sorted(self))
