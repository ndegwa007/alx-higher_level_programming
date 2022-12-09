#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_d = {}
    new_d.update(a_dictionary)
    for key in new_d.keys():
        new_d[key] *= 2
    return new_d
