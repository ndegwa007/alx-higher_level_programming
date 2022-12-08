#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    update = {key: value}
    for key, value in a_dictionary.items():
        if key not in a_dictionary:
            a_dictionary[key] = value
        else:
            a_dictionary[key].update(update)
    return a_dictionary
