#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_score = 0
    for name, score in a_dictionary.items():
        if score > best_score:
            best_score = score
    for name, score in a_dictionary.items():
        if a_dictionary[name] == best_score:
            return name
