#!/usr/bin/python3
def no_c(my_string):
    if "c" not in my_string and "C" not in my_string:
        return my_string
    else:
        return my_string.translate({ord(i): None for i in "cC"})
