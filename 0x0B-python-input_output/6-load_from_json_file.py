#!/usr/bin/python3
"""
import json module
"""
import json


def load_from_json_file(filename):
    """
    creates an obj from JSON file
    """
    with open(filename, encoding="utf-8") as f:
        json_data = f.read()
        return json.loads(json_data)
