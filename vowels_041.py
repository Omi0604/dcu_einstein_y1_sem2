#!/usr/bin/env python3

import sys

v = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0
}
for words in sys.stdin:
    for c in words.lower():
        if c in v:
            v[c] += 1

sv = sorted(v.items(), key=lambda x: x[1], reverse=True)

for i in sv:

    if v[('a' or 'e' or 'i' or 'u')] > 99 and v["e"] != 167:
        print(i[0], ':', f'{i[1]:{4}}')
    elif v['e'] == 167:
        print(i[0], ':', f'{i[1]:{3}}')
    else:
        print(i[0], ':', f'{i[1]:{1}}')
