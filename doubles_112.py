#!/usr/bin/env python3

import sys

dict = {}


def doubles(line):
    vowels = "aeiou"
    i = 0
    total = 0
    line = line.strip()
    while i < len(line):
        if (line[i - 1] == line[i]) and (line[i] in vowels):
            total = total + 1
        i = i + 1
    dict[line] = total


for input in sys.stdin:
    doubles(input)

print(max(dict, key=dict.get))
