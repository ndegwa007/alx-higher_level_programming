#!/usr/bin/python3
"""find a peak in a list of unsorted intergers"""


def find_peak(list_of_integers: [int]) -> int:
    """gets a peak integer in the list"""
    # first set index values
    low = 0
    high = len(list_of_integers) - 1

    # check null case
    if len(list_of_integers) == 0:
        return None
    # check for duplicates
    for i in list_of_integers:
        if list_of_integers.count(i) == len(list_of_integers):
            return i

    # loop to get mid and return value in the list
    while (low <= high):
        mid = (low + high) // 2

        if (mid > 0 or list_of_integers[mid] > list_of_integers[mid + 1]) and \
                (mid == high or
                    list_of_integers[mid] > list_of_integers[mid - 1]):
            return list_of_integers[mid]

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid - 1
