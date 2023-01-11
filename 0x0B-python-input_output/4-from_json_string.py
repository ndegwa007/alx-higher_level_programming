#!/usr/bin/python3

"""import from json module """
import json


def from_json_string(my_str):
    """
    return an object (python data structure)
    represented by a JSON string
    """
    return json.loads(my_str)
