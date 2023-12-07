#!/usr/bin/python3
def roman_to_int(roman_string):
    sample = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not roman_string:
        return 0
    list(roman_string)
    length = len(roman_string)
    i = 0
    count = 0
    while i < length:
        if length == 1:
            count = sample[roman_string[i]]
            break
        if i + 1 <= length - 1:
            if sample[roman_string[i]] < sample[roman_string[i + 1]]:
                count = (sample[roman_string[i + 1]] - sample[roman_string[i]])
                i += 1
            else:
                count = sample[roman_string[i]]
        count += count
        i += 1
    return count
