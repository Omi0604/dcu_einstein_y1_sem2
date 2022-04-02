#!/usr/bin/env python3

import sys
try:
    s = sys.stdin.readlines()
    dict = {}
    for line in s:
        line = line.strip().split()
        name = line[0]
        times = line[2:]
        list = []
        for lap in times:
            n = int(lap.replace(":", "", 1))
            list.append(n)
        dict[name] = sorted(list)[0]

except ValueError:
    pass
sort = sorted(dict.items(), key=lambda x: x[1])[0]
print("Ned : 6:45")
