#!/usr/bin/python3
"""Define class rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define class square"""

    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
