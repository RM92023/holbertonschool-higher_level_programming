#!/usr/bin/python3
"""Define the Base Class"""


class Base:
    """constructor"""
    __nb_objects = 0

    """Function Initialized"""

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects