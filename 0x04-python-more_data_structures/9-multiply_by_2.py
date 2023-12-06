#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_a_dictionary = a_dictionary.copy()
    for key in new_a_dictionary.keys():
        if new_a_dictionary[key] >= 0 and new_a_dictionary[key] <= 9:
            new_a_dictionary[key] = new_a_dictionary[key] * 2
    return new_a_dictionary
