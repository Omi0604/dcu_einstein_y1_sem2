#!/usr/bin/env python3

import sys
words = sys.stdin.readlines()

with open(sys.argv[1], "r") as f:
    s = f.readlines()

for line in words:
    line = line.strip().split()
    i = 0
    while i < len(line):
        word = line[i]
        for censor in s:
            censor = censor.rstrip()
            if censor in word:
                line[i] = word.replace(censor, "@" * len(censor))
        i += 1
    print(" ".join(line))
