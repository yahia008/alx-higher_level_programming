#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set_1 | set_2
    return {ele for ele in new_set if ele in set_1 and ele not in set_2 or
