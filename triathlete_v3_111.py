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


def main():

    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    t2.add_time('swim', 300)
    t2.add_time('cycle', 100)
    t2.add_time('run', 200)

    t3.add_time('swim', 150)
    t3.add_time('cycle', 120)
    t3.add_time('run', 100)

    print(t1)
    print(t2)
    print(t3)

    assert(t1 == t3)
    assert(t1 < t2)
    assert(t2 > t3)


if __name__ == '__main__':
    main()
