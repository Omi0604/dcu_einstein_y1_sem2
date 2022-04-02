#!/usr/bin/env python3

def swap_unique_keys_values(d):
    dict = {}
    for k, v in d.items():
        if v not in dict:
            dict[v] = k, 1
        else:
            dict[v] = k, dict[v][1] + 1
    output = {}
    for k, v in dict.items():
        if dict[k][1] == 1:
            output[k] = dict[k][0]
    return output
