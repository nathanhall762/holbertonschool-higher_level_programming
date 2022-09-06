#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    result = 0
    for idx in my_list:
        if idx not in new_list:
            new_list.append(idx)
    for idx2 in new_list:
        result += idx2
    return result
