#!/usr/bin/python3
# Print all possible combinations of two digits
for i in range(10):
    for j in range(i+1, 10):
        print("{}{}".format(i, j), end=", " if i < 8 else "\n")
