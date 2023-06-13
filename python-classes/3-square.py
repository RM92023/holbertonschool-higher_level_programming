#!/usr/bin/python3
"""
Define Squeare with area
"""


class Square:
    """
    define constructor with area
    """
    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise ValueError("size must be an integer")

    """
    Define function or object with area
    """
    def area(self):
        return self.__size ** 2
