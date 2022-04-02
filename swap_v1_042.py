#!/usr/bin/env python3

def swap_keys_values(dict):
    newdict = {}
    for a, b in dict.items():
        newdict[b] = a
    return newdict
