#!/usr/bin/python3
from dis import dis
def magic_calculation(a, b):
     from magic_calculation_102 import add, sub
     if a > b:
        c = add(a, b)

print(dis(magic_calculation))
