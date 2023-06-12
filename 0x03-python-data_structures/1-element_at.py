#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return(None)
    length = len(my_list) - 1
    if idx > length:
        return(None)
    if my_list[idx]:
        athere = my_list[idx]
        return(athere)
