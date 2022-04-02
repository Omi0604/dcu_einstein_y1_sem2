#!/usr/bin/env python3

import sys

def nice(s):
    s = s.strip()
    nice = "nice"
    a = []
    for letter in s:
        if letter in nice:
            a.append(letter)
    if len(a) == 4:
        print(s)


for word in sys.stdin:
    nice(word)
