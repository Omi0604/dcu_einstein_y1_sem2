#!/usr/bin/env python3

import sys

r = {
    'A': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0,
    'T': 0,
    'J': 0,
    'Q': 0,
    'K': 0,
}

for hand in sys.stdin:
    hand = hand.replace(" ", "")
    for i in hand:
        if i in r:
            r[i] += 1

m_v = max(r, key=r.get)
print(r[m_v])
