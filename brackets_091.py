#!/usr/bin/env python3

def matcher(s):
    count1 = 0
    count2 = 0
    count3 = 0
    for bracket in s:
        if bracket == "(":
            count1 += 1
        elif bracket == ")":
            count1 -= 1
        elif bracket == "[":
            count2 += 1
        elif bracket == "]":
            count2 -= 1
        elif bracket == "{":
            count3 += 1
        elif bracket == "}":
            count3 -= 1
    return (count1 == 0 and count2 == 0 and count3 == 0)
