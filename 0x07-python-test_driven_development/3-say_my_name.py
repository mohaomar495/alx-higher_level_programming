#!/usr/bin/python3
""" This prints the first and last name """


def say_my_name(first_name, last_name=""):
    """
    Print the given name as its whether its full name with first and last name
    or just the first name.

    args:
        first_name: str
        last_name: str
    raises:
        TypeError if both are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
