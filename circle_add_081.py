#!/usr/bin/env python3

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def midpoint(self, other):
        return Point(((self.x + other.x) / 2), ((self.y + other.y) / 2))

    def __str__(self):
        return (f"({self.x:.1f}, {self.y:.1f})")


class Circle():
    def __init__(self, centre=None, radius=1):
        self.centre = Point() if centre is None else centre
        self.radius = radius

    def __str__(self):
        return (f"Centre: {self.centre}\nRadius: {self.radius}")

    def __add__(self, other):
        radius = self.radius + other.radius
        centre = self.centre.midpoint(other.centre)
        return Circle(centre, radius)
