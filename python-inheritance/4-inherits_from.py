#!/usr/bin/python3
"""Define inheritance for classes"""


def inherits_from(obj, a_class):
    """define type inheritance"""
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    return False
