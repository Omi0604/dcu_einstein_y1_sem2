#!/usr/bin/env python3

class Student(object):
    def __init__(self, name, cao):
        self.name = name
        self.cao = cao
        self.dict = {}

    def __str__(self):
        return (f"Name: {self.name}\nCAO: {self.cao}")

    def add_grade(self, subject, grade):
        self.dict[subject] = grade

    def get_grade(self, subject):
        if subject in self.dict:
            return self.dict[subject]
        else:
            return f"N/A"
