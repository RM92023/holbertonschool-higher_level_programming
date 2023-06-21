#!/usr/bin/python3
"""Define class empty"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class base class for Geometry"""

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
