#!/usr/bin/python3
def uniq_add(my_list=[]):
    output = set()
    for i in my_list:
        output.add(i)
    return sum(output)
