#!/usr/bin/env python3

def maximum(l):
    if len(l) == 1:
        return l[0]
    maxNumber = maximum(l[1:])
    max = l[0]
    if maxNumber > max:
        max = maxNumber
    return max
