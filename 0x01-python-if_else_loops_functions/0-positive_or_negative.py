#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number is not None:
    if number == 0:
        print(f"{number} is zero")
    elif number < 0:
        print(f"{number:d} is negative")
    elif number > 0:
        print(f"{number:d} is positive")
