#!/usr/bin/python3
"""Defin class square"""


class Square:
    """A square object"""
    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise ValueError("size must be an integer")
