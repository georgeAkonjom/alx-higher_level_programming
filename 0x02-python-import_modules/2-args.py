#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arg_no = len(argv) - 1
    output = ""

    if arg_no == 0:
        output = f"{arg_no} argument{'s' if arg_no != 1 else ''}."
    else:
        output = f"{arg_no} argument{'s' if arg_no != 1 else ''}:"

    print(output)

    for i in range(1, len(argv)):
        arg = argv[i]
        print(f"{i}: {arg}")
