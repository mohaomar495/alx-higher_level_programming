#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if my_list is None:
        my_list = []

    num_printed_elems = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num_printed_elems += 1
        except (ValueError, TypeError):
            continue
    print()
    return num_printed_elems
