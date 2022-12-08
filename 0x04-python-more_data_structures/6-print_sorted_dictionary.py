#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = sorted(a_dictionary.items())
    for i in dict(a).items():
        print("{}: {}".format(i[0], i[1]))
