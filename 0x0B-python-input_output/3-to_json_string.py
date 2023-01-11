#!/usr/bin/python3
import json
"""
a module with a function
the functionn returns JSON representation of an obj(str)
"""


def to_json_string(myobj):
    """
    return JSON rep of an object
    """
    return json.dumps(myobj)
