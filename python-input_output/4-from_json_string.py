#!/usr/bin/python3
"""defines the json module"""


import json


def from_json_string(my_str):
    """returns a json strinn loads my_str"""
    return json.loads(my_str)
