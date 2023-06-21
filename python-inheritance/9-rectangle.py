#!/usr/bin/python3
"""Define Base Geometry class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """define initialization"""

    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return f"[Rectangle] {self.width}/{self.height}"

    def __str__(self):
        return self.__repr__()
