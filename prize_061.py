#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()
location = int(s[0].strip())

for char in s[1]:
    if char == "A" and location == 2:
        location = location - 1
    elif char == "A" and location == 1:
        location = location + 1
    elif char == "B" and location == 2:
        location = location + 1
    elif char == "B" and location == 3:
        location = location - 1
    elif char == "C" and location == 1:
        location = location + 2
    elif char == "C" and location == 3:
        location = location - 2
print(location)
