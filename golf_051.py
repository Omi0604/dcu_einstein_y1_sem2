#!/usr/bin/env python3

import sys

def sorter(n):
    return n[1]


list = []
dict = {}
for lines in sys.stdin:
    total = 0
    lines = lines.strip().split()
    name = " ".join(lines[:-3])
    goals = "".join(lines[-3:])
    goals_confirmed = ""
    for goal in goals:
        if goal.isdigit() is False:
            list.append(name)
        else:
            goals_confirmed = goals_confirmed + " " + goal
    goals_confirmed = goals_confirmed.split()
    for n in goals_confirmed:
        n = int(n)
        total = n + total
    dict[name] = total
for name in list:
    if name in dict:
        dict.pop(name)

for key, n in sorted(dict.items(), key=sorter):
    print(f"{key}: {n}")
if len(list) > 0:
    print(f"Disqualified: {', '.join(list)}")
