#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list is None:
        my_list = []
    num_printed_elems = 0

    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            num_printed_elems += 1
    except IndexError:
        pass
    finally:
        print()
        return num_printed_elems
