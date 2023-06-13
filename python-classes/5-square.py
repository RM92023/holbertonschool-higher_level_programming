#!/usr/bin/python3
"""
Define class Square
"""


class Square:
    """
    Define a square
    """
    def __init__(self, size=0):
        self.__size = size

    """
    Method gets called
    """
    @property
    def size(self):
        return self.__size

    """
    method sets called
    """
    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    """
    Method Area called
    """
    def area(self):
        return self.__size ** 2

    """
    Method my_print called
    """
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
