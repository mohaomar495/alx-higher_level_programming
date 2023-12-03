#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in my_list:
        if i >= 0 and i <= 9:
            print("{}".format(i))
