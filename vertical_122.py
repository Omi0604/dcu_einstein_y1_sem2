#!/usr/bin/env python3
import sys
s = sys.stdin.readlines()

# takes input 1 letter per word and appends to a list
a = []
i = 0
while i < len(s[0].strip()):
    for input in s:
        a.append(input[i])
    i = i + 1

# converts the letters into words
new_list = []
i = 0
while i < len(s[0].strip()):
    new_list.append("".join(a[:len(s)]))
    del a[:len(s)]
    i = i + 1

# sorts the list while ignoring cases, and returns new list with sorted elements and cases intact
new_list = sorted(new_list, key=str.casefold)

# makes the words vertical again
a = []
i = 0
while i < len(new_list[0]):
    for word in new_list:
        a.append(word[i])
    i = i + 1

# converts letters back into words
i = 0
while i < len(new_list[0]):
    a.append("".join(a[:len(new_list)]))
    del a[:len(new_list)]
    i = i + 1

for word in a:
    print(word)
