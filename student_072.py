#!/usr/bin/env python3

class Student():

    def __init__(self, sid, name, modlist=[]):
        self.sid = sid
        self.name = name
        self.modlist = modlist.copy()

    def add_module(self, module):
        if module not in self.modlist:
            self.modlist.append(module)

    def del_module(self, module):
        if module in self.modlist:
            self.modlist.remove(module)

    def __str__(self):
        return (f"ID: {self.sid}\nName: {self.name}\nModules: {', '.join(self.modlist)}")
