#!/usr/bin/python3
"""Describe the load json file"""


import json


def load_from_json_file(filename):
    """Load json file"""
    with open(filename, 'r') as f:
        return json.load(f)
