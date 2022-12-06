#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_l = []
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    for i in range(len(my_list)):
        if i != idx:
            new_l.append(my_list[i])
        else:
            new_l.append(element)
    return new_l
