#!/usr/bin/python3
def multiple_returns(sentence):
    t = tuple(sentence)
    if sentence == "":
        t[0] == None
    return len(t), t[0]
