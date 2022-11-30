#!/usr/bin/python3
def islower(c):
    # loop c
    for i in c:
        if 97 <= ord(i) <= 123:
            return True
        else:
            return False
