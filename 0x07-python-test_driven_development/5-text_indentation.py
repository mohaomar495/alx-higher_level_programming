#!/usr/bin/python3
"""Definition of a function that prints a text
with 2 new lines after each of these characters: ., ? and : """


def text_indentation(text):
    """
    :param text: str
    :return: text with two new lines after each of these characters: . ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = []
    i = 0
    while i < len(text) and text[i] == " ":
        i += 1
    while i < len(text):
        char = text[i]
        result.append(char)
        if char in ".:?":
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1
            result.append("\n\n")
        i += 1
    print("".join(result))
