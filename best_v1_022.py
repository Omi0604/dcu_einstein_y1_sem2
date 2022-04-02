#!/usr/bin/env python3

from os import name
import sys

with open(sys.argv[1], "r") as f:
    f = f.readlines()

dict = {}
highest = 0
try:
    for line in f:
        line = line.strip().split()
        marks = int(line[0])
        name = " ".join(line[1:])
        if marks not in dict.keys():
            dict[marks] = name
        if marks > highest:
            highest = marks
except FileNotFoundError:
    print(f"The file (filename) could not be opened.")

print("Best student:", dict[highest])
print("Best mark:", highest)
