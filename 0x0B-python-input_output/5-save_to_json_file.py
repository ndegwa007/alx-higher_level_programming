#!/usr/bin/python3

""" import json module """
import json


def save_to_json_file(my_obj, filename):

    """
    save_to_json_file: writes an obect to a text file
                    using json representationn
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(json.dumps(my_obj))
