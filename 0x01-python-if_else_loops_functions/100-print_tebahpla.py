#!/usr/bin/python3
output = ""
for i in range(ord('z'), ord('a') - 1, -1):
    letter = chr(i)
    if i % 2 == 0:
        output += "{}".format(letter.lower())
    else:
        output += "{}".format(letter.upper())

print("{}".format(output), end="")
