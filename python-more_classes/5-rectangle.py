#!/usr/bin/python3
"""Define class Rectangle"""


class Rectangle:
    """Construct"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

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

    """Define Area"""
    def area(self):
        return self.__width * self.__height

    """Define Perimeter"""
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    """Define print and string"""
    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        rectangle = ""
        for _ in range(self.height):
            rectangle += "#" * self.width + "\n"
        return rectangle[:-1]

    """Define repr and eval"""
    def __repr__(self):
        return f"Rectangle(%d, %d)" % (self.width, self.height)

    """Delete dots ellipsis"""
    def __del__(self):
        print("Bye rectangle...")
