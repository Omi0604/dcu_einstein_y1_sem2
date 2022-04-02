#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
    lines = []
    for line in f:
        line = line.strip()
        lines.append(line)
with open(sys.argv[2], "r") as f:
    for line in f:
        line = line.strip()
        lines.append(line)

i = 0
while i < len(lines) // 2:
    print(lines[i])
    print(lines[i + len(lines) // 2])
    i = i + 1
