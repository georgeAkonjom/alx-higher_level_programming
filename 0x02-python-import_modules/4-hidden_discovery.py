#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for eachname in dir(hidden_4):
        if eachname.startswith("__"):
            continue
        else:
            print(eachname)
