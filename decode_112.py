#!/usr/bin/env python3

import sys


def decode(s):
    vowels = "aeiou"
    s = s.strip()
    a = []
    i = 0
    while i < len(s):
        if s[i] in vowels:
            a.append(s[i])
            i = i + 3
        else:
            a.append(s[i])
            i = i + 1
    print("".join(a))


for input in sys.stdin:
    decode(input)
