#!/usr/bin/python3
i = 0
for char in range(122, 96, -1):
    print(f"{chr(char - i)}", end="")
    if i == 0:
        i = 32
    else:
        i = 0
