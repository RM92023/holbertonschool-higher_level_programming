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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    """setter height"""

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    """setter x"""

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    """Setter y"""

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    """Adding Area to the rectangle"""

    def area(self):
        """Add a new area to the rectangle"""
        return self.__width * self.__height
    

    """Adding display # in the rectangle"""
    def display(self):
        """adding loops for the print rectangle"""
        for _ in range(self.__height):
            print("#" * self.__width)
