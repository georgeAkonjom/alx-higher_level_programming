#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        i = chr(i)
        print(i)
    else:
        i = chr(i)
        print(i.upper())
