#!/usr/bin/python3
"""class Square import class Rectangle"""
from models.rectangle import Rectangle


"""Create class Square"""


class Square(Rectangle):
    """Create constructor for square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    """print constructor"""

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    """Getter for square"""
    @property
    def size(self):
        return self.width

    """setter for square"""
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
