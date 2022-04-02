#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

d = []
a = []
i = 0
while i < len(lines):
    a.append(lines[i])
    i = i + 1
    if i < len(lines):
        d.append(lines[i])
    i = i + 1
for line in a:
    print(line.strip())
for line in d[::-1]:
    print(line.strip())
