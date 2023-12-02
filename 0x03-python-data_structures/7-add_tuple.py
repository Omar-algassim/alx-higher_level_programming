#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuplelen = len(tuple_b)
    if tuplelen < 2:
        while len(tuple_b) < 2:
            tuple_b = tuple_b + (0,)
        
    new = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new