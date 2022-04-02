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


def main():

    t1 = Triathlete('Ian Brown', 21)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    print('Cycle: {}'.format(t1.get_time('cycle')))
    print(t1)


if __name__ == '__main__':
    main()
