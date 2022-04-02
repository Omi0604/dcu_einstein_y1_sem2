#!/usr/bin/env python3

import sys
import calendar

def birthday(s):
    s = s.split()
    day = calendar.weekday(int(s[2]), int(s[1]), int(s[0]))
    if day == 0:
        print("You were born on a Monday and Monday's child is fair of face.")
    elif day == 1:
        print("You were born on a Tuesday and Tuesday's child is full of grace.")
    elif day == 2:
        print("You were born on a Wednesday and Wednesday's child is full of woe.")
    elif day == 3:
        print("You were born on a Thursday and Thursday's child has far to go.")
    elif day == 4:
        print("You were born on a Friday and Friday's child is loving and giving.")
    elif day == 5:
        print("You were born on a Saturday and Saturday's child works hard for a living.")
    else:
        print("You were born on a Sunday and Sunday's child is fair and wise and good in every way.")
    return


for s in sys.stdin:
    birthday(s)
