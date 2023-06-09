#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        operator = argv[2]

        if operator == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
        if operator == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
        if operator == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
        if operator == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
        if not any(item in argv for item in ['+', '-', '*', '/']):
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
