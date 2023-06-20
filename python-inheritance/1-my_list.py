#!/usr/bin/python3
"""Define class MyList"""


class MyList(list):
    """define a function that print sorted list"""
    def print_sorted(self):
        sortedList = sorted(self)
        print(sortedList)
