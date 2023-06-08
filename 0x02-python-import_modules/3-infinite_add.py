#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    result = 0
    arg_no = len(argv)
    for i in range(1, arg_no):
        args = int(argv[i])
        result += args
    print(result)
