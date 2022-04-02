#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()

word = s[0].strip()
word_list = s[1:]

a = []
for element in word_list:
    if len(word) == len(element.strip()):
        i = 0
        j = 0
        for letter in word:
            if letter == "-":
                j = j + 1
            if letter != "-" and letter in element.strip():
                i = i + 1
        if i == len(word) - j:
            a.append(element.strip())

print(", ".join(a))
