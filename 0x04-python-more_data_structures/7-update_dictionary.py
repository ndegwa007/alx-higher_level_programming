#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    dict_list = [key, value]
    if key not in a_dictionary:
        a_dictionary.update([dict_list])
    else:
        a_dictionary[key] = value

    return a_dictionary
