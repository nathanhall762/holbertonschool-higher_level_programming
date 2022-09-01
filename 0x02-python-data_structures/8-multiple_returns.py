#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence[0] = None
    new_tuple = (len(sentence), sentence[0])
    return new_tuple
