#!/usr/bin/env python3

import sys
from string import punctuation

seen = {}
lines = sys.stdin.readlines()
for line in lines:
    words = line.split()
    for i, word in enumerate(words):
        word = word.lower().strip(punctuation)
        if word not in seen:
            seen[word] = True
        else:
            words[i] = "."
    print(" ".join(words))
