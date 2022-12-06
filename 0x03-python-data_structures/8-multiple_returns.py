#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return None
    t = tuple(sentence)
    return len(t), t[0]
