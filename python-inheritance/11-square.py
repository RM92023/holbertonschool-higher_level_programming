#!/usr/bin/python3
"""define import path"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """define _init function"""

    def __init__(self, size):
        self._size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        return f"[Square] {self._size}/{self._size}"
