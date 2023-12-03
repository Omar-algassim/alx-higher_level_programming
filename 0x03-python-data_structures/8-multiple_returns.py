#!/usr/bin/python3
def multiple_returns(sentence):
    ret_tuple = ()
    length = len(sentence)
    if length == 0:
        first = None
        ret_tuple = (length, first)
        return ret
    else:
        ret_tuple = (length, sentence[0])
        return ret_tuple
