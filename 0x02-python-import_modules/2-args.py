#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arg_no = len(argv) - 1
    output = ""
    if arg_no:
        output = f"{arg_no} arguments:"
    if arg_no == 1:
        output = f"{arg_no} argument:"
    if arg_no == 0:
        output = f"{arg_no} arguments."
    print("{}".format(output))
    for i in range(arg_no + 1):
        arg = argv[i]
        if i == 0:
            continue
        else:
            print("{}: {}".format(i, arg))        
