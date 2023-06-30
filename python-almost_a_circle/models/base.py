#!/usr/bin/python3
"""Define the Base Class"""

import turtle
from turtle import *


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

    @staticmethod
    def to_json_string(list_dictionaries):
        import json
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + '.json'
        with open(filename, 'w') as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                list_dict = [o.to_dictionary() for o in list_objs]
                json_file.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        import json
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        turtle.reset()
        turtleDraw = turtle.Turtle()
        turtleDraw.screen.bgcolor("#888888")
        turtleDraw.pensize(3)

        turtleDraw.color("#FFA500")
        for rect in list_rectangles:
            turtleDraw.showturtle()
            turtleDraw.up()
            turtleDraw.goto(rect.x, rect.y)
            turtleDraw.down()
            for i in range(2):
                turtleDraw.forward(rect.width)
                turtleDraw.left(90)
                turtleDraw.forward(rect.height)
                turtleDraw.left(90)
            turtleDraw.hideturtle()

        turtleDraw.color("#b5e3d8")
        for square in list_squares:
            turtleDraw.showturtle()
            turtleDraw.up()
            turtleDraw.goto(square.x, square.y)
            turtleDraw.down()
            for i in range(2):
                turtleDraw.forward(square.width)
                turtleDraw.right(-90)
                turtleDraw.forward(square.height)
                turtleDraw.right(-90)
            turtleDraw.hideturtle()

        turtle.exitonclick()
