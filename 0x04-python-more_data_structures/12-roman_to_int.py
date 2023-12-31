#!/usr/bin/python3
def roman_to_int(roman_string):
    sample = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not isinstance(roman_string, str) and not None:
        return 0
    list(roman_string)
    length = len(roman_string)
    i = 0
    count = 0
    add = 0
    while i < length:
        if length == 1:
            count = sample[roman_string[i]]
            return count
        elif i + 1 <= length - 1:
            if sample[roman_string[i]] < sample[roman_string[i + 1]]:
                add = (sample[roman_string[i + 1]] - sample[roman_string[i]])
                i += 1
            else:
                add = sample[roman_string[i]]
        else:
            add = sample[roman_string[i]]
        count += add
        i += 1
    return count
