#!/usr/bin/python3
"""Define read file"""


def read_file(filename=""):
    """Define open file"""
    with open(filename, encoding='UTF8') as f:
        print(f.read(), end='\n')
