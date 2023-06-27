#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    final = 0
    for elem in range(x):
        try:
            print(my_list[elem], end="")
            final += 1
        except IndexError:
            print()
            return(final)
    print()
    return(final)
