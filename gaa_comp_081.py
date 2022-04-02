#!/usr/bin/env python3

class Score():

    def __init__(self, goals=0, points=0, score=0):
        self.goals = goals
        self.points = points
        self.score = self.goals * 3 + self.points

    def __str__(self):
        return (f"{self.goals} goal(s) and {self.points} point(s)")

    def __eq__(self, other):
        return ((self.score) == (other.score))

    def __gt__(self, other):
        return ((self.score) > (other.score))

    def __ge__(self, other):
        return ((self.score) >= (other.score))

    def __lt__(self, other):
        return ((self.score) < (other.score))

    def __le__(self, other):
        return ((self.score) <= (other.score))
