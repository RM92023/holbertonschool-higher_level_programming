#!/usr/bin/python3
""" Describe save to json file. """


import json


def save_to_json_file(my_obj, filename):
    """ Save to json file. """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
        return (f)
