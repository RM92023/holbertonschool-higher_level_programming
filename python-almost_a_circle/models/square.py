#!/usr/bin/python3
"""class Square import class Rectangle"""
from models.rectangle import Rectangle


"""Create class Square"""


class Square(Rectangle):
    """Create constructor for square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
