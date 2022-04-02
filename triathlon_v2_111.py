#!/usr/bin/env python3

class Triathlete(object):
    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        return (f"Name: {self.name}\nID: {self.tid}")


def checker(item):
    return item.name


class Triathlon():
    def __init__(self):
        self.d = {}

    def add(self, other):
        self.d[other.tid] = other

    def remove(self, tid):
        self.d.pop(tid)

    def lookup(self, tid):
        if tid in self.d.keys():
            return self.d[tid]
        return None

    def __str__(self):
        a = [f"{t}" for t in sorted(self.d.values(), key=checker)]
        return "\n".join(a)
