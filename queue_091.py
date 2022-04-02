#!/usr/bin/env python3

class Queue(object):
    def __init__(self):
        self.list = []

    def enqueue(self, e):
        return self.list.append(e)

    def dequeue(self):
        return self.list.pop(0)

    def first(self):
        return self.list[0]

    def is_empty(self):
        return len(self.list) == 0

    def __len__(self):
        return len(self.list)
