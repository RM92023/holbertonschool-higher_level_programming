#!/usr/bin/python3
"""define the append method"""


def append_write(filename="", text=""):
    """describe the append method"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
