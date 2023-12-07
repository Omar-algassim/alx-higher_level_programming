#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        comp = 0
        string = ''
        for i in a_dictionary:
            if a_dictionary[i] is not None:
                if comp < a_dictionary[i]:
                    comp = a_dictionary[i]
                    string = i
            else:
                return None                
        return string
    else:
        return None
