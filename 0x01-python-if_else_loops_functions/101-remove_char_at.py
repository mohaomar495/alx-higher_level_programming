#!/usr/bin/python3
def remove_char_at(str, n):
    if len(str) > n:
        return (f"{str.replace(str[n], '')}")
    else:
        return str
