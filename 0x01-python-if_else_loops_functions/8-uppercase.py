#!/usr/bin/python3
def uppercase(s):
    for c in s:
        ascii_val = ord(c)
        if 97 <= ascii_val <= 122:
            ascii_val -= 32
        print("{:c}".format(ascii_val), end="")
    print("", end="\n")
