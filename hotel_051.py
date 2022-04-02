#!/usr/bin/env python3

import sys

def hotel(s):
    s = s.strip().split()
    total_rooms = int(s[0])
    taken_rooms = s[1:]
    taken_rooms = [int(i) for i in taken_rooms]
    r = range(1, total_rooms + 1)
    available_rooms = [rooms for rooms in r if rooms not in taken_rooms]
    if len(available_rooms) == 0:
        print("no room")
    else:
        print(sorted(available_rooms)[0])


for lines in sys.stdin:
    hotel(lines)
