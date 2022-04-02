#!/usr/bin/env python3

class Contact():
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return (f"{self.name} {self.phone} {self.email}")

class ContactList():
    def __init__(self):
        self.d = {}

    def add(self, c):
        self.d[c.name] = c

    def remove(self, name):
        if name in self.d:
            del(self.d[name])

    def get(self, name):
        if name in self.d:
            return self.d[name]
        else:
            return None

    def __str__(self):
        slist = []
        slist.append("Contact list")
        slist.append("------------")
        for k, v in sorted(self.d.items()):
            slist.append(f"{v}")
        return "\n".join(slist)
