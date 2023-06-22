#!/usr/bin/python3
"""Define read file"""


def read_file(filename=""):
    """Define open file"""
    with open('my_file_0.txt', 'r', encoding='UTF8') as f:
        content = f.read()
        print(content)
