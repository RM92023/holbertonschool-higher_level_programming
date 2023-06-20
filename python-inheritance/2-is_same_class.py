#!/usr/bin/python3
"""Define Same class with objects"""


def is_same_class(obj, a_class):
    """Returns if the object is exactly an instance of the specified class"""
    if not isinstance(obj, a_class):
        return False

    class_type = type(obj)
    if class_type is a_class:
        return True
    else:
        return False
