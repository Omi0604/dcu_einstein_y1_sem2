#!/usr/bin/env python3

class Meeting():
    def __init__(self, hour, minute, duration):
        self.hour = hour
        self.minute = minute
        self.duration = duration

    def __str__(self):
        return (f"{self.hour:02d}:{self.minute:02d} ({self.duration} minutes)")

class Schedule():
    def __init__(self):
        self.schedule = []

    def add(self, m):
        self.schedule.append(m)

    def __str__(self):
        slist = []
        for meeting in self.schedule:
            slist.append(f'{meeting}')
        slist2 = []
        slist2.append("Schedule")
        slist2.append("--------")
        for meeting in sorted(slist):
            slist2.append(f"{meeting}")
        slist2.append(f"Meetings today: {len(self.schedule)}")
        return "\n".join(slist2)
