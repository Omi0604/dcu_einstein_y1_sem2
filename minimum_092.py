#!/usr/bin/env python3

def minimum(l):
    if len(l) == 1:
        return l[0]
    minNumber = minimum(l[1:])
    min = l[0]
    if minNumber < min:
        min = minNumber
    return min
