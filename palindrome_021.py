#!/usr/bin/env python3

import sys

def palindrome(s):
    s = s.strip().lower()
    keep = []
    for c in s:
        if c.isalnum():
            keep.append(c)
    return keep == keep[::-1]


for s in sys.stdin:
    print(palindrome(s))
