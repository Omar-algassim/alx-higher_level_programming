#!/usr/bin/python3
def roman_to_int(roman_string):
    sample = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list(roman_string)
    length = len(roman_string)
    count = 0
    for i in range(length):
        if i + 1 < length - 1:
            if sample[roman_string[i]] < sample[roman_string[i + 1]]:
                count += (sample[roman_string[i]] - sample[roman_string[i + 1]])
                i + 1
                print(i)
        count += sample[roman_string[i]]
    return count
