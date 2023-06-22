#!/usr/bin/python3
"""defines the json module"""


import json


def to_json_string(my_obj):
    """returns a json string representation of my_obj"""
    return json.dumps(my_obj)
