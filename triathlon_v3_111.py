#!/usr/bin/env python3

class Triathlete(object):
    def __init__(self, name, tid, swim=0, cycle=0, run=0):
        self.name = name
        self.tid = tid
        self.swim = swim
        self.cycle = cycle
        self.run = run

    def __str__(self):
        total_time = self.swim + self.cycle + self.run
        return (f"Name: {self.name}\nID: {self.tid}\nRace time: {total_time}")

    def add_time(self, game, time):
        if game == "swim":
            self.swim = time
        elif game == "cycle":
            self.cycle = time
        else:
            self.run = time

    def get_time(self, game):
        if game == "swim":
            return self.swim
        elif game == "cycle":
            return self.cycle
        else:
            return self.run

    def __eq__(t1, t2):
        return ((t1.swim == t2.swim) or (t1.run == t2.run) or (t1.cycle == t2.cycle))

    def __lt__(t1, t2):
        return ((t1.run < t2.run) or (t1.cycle < t2.cycle) or (t1.swim < t2.swim))

    def __gt__(t1, t2):
        return ((t1.run > t2.run) or (t1.cycle > t2.cycle) or (t1.swim > t2.swim))


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

    def best(self):
        return min(self.d.values())

    def worst(self):
        return max(self.d.values())
