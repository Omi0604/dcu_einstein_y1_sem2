#!/usr/bin/env python3

import sys

contact = {}
with open(sys.argv[1], "r") as f:
    contacts = f.readlines()
    for line in contacts:
        name, number = line.strip().split()
        contact[name] = number

for name in sys.stdin:
    try:
        print(f'Name: {name.strip()}')
        print(f'Phone: {contact[name.strip()]}')
    except KeyError:
        print(f'No such contact')
