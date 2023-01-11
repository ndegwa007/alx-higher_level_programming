#!/usr/bin/python3
"""module: load from json file"""
import json


def to_json_string(myobj):
    """
    return JSON rep of an object
    """
    return json.dumps(myobj)
