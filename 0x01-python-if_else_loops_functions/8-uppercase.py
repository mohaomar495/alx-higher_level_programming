#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if (ord(str[i]) >= 97 and ord(str[i]) <= 122):
            i = (ord(str[i]) - 32)
        print("{}".format(chr(i)), end="")
    print("")

