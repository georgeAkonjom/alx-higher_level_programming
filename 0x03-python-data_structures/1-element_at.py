#!/usr/bin/python3
def element_at(my_list, idx):
    for i in range(len(my_list)):
        if idx > i:
            return(None)
    if idx < 0:
        return(None)
    if my_list[idx]:
        athere = my_list[idx]
        return(athere)
