#!/usr/bin/python3
"""Define class rectangle"""


from models.base import Base

"""define class rectangle with base class"""


class Rectangle(Base):
    """define init in class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)


"""get width"""


@property
def width(self):
    return self.__width


"""get height"""


@property
def height(self):
    return self.__height


"""get x"""


@property
def x(self):
    return self.__x


"""get y"""


@property
def y(self):
    return self.__y


"""setter width"""


@width.setter
def width(self, value):
    self.width = value


"""setter height"""


@height.setter
def height(self, value):
    self.height = value


"""setter x"""


@x.setter
def x(self, value):
    self.x = value


"""Setter y"""


@y.setter
def y(self, value):
    self.y = value
