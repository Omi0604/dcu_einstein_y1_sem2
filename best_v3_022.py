#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
    f = f.readlines()

dict = {}
highest = 0

for line in f:
    try:
        line = line.strip().split()
        marks = int(line[0])
        name = " ".join(line[1:])
        if marks not in dict.keys():
            dict[marks] = name
        if marks > highest:
            highest = marks
    except ValueError:
        print(f"Invalid mark {line[0]} encountered. Skipping.")

print("Best student:", dict[highest])
print("Best mark:", highest)
