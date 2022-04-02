#!/usr/bin/env python3

class Student(object):
    def __init__(self, name, cao):
        self.name = name
        self.cao = cao

    def __str__(self):
        return (f"Name: {self.name}\nCAO: {self.cao}")

def checker(item):
    return item.name

class Classlist(object):
    def __init__(self):
        self.dict = {}

    def add(self, other):
        self.dict[other.cao] = other

    def remove(self, cao):
        if cao in self.dict.keys():
            self.dict.pop(cao)

    def lookup(self, cao):
        if cao in self.dict.keys():
            return self.dict[cao]
        else:
            return None

    def __str__(self):
        a = [f"{self.dict[t]}" for t in sorted(self.dict.keys())]
        return "\n".join(a)
