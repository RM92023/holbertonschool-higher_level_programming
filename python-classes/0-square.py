#!/usr/bin/python3
"""
define class called Square
"""


class Square:
    def __init__(self):
        """
        Initialization method of the Square class.
        Called automatically when a new object of the Square class is created.
        """
        Square.square = None
        """
        Sets the "square" attribute of the Square class to None.
        This attribute is shared by all objects of the class,
        since you are assigning directly to the class instead
        of a specific instance.
        """
