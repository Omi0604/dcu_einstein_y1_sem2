#!/usr/bin/env python3

def reverse_list(s):
    if s == []:
        return []
    return [s[-1]] + reverse_list(s[:-1])
