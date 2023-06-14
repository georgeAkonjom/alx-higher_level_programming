#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list) - 1
    if my_list:
        while length > 1:
            j = 0
            while j < length:
                if my_list[j] > my_list[j + 1]:
                    buffer = my_list[j]
                    my_list[j] = my_list[j + 1]
                    my_list[j] = buffer
                j += 1
            length -= 1
        return(my_list[length])
    else:
        return(None)
