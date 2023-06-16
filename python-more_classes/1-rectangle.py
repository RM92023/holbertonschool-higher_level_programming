#!/usr/bin/python3
"""Define class Rectangle"""


class Rectangle:
    """Construct"""
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    """Get Width"""
    @property
    def width(self):
        return self.__width

    """Set Width"""
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """get Height"""
    @property
    def height(self):
        return self.__height

    """set Height"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
