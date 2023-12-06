#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        sorted(a_dictionary)
        comp = 0
        string = ''
        for i in a_dictionary:
            if comp < a_dictionary[i]:
                comp = a_dictionary[i]
                string = i
                print(string)
        return string
    return None
    
