#!/usr/bin/env python3

import sys
import string

def unique(s):
    unique_ls = list()
    for token in s:
        for char in token:
            if char in string.punctuation:
                token = token.replace(char, "")
        if token != "" and token not in unique_ls:
            unique_ls.append(token)
    return len(unique_ls)


s = sys.stdin.read().lower().strip().split()
print(unique(s))
