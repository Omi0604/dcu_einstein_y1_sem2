#!/usr/bin/env python3

class Student():

    def __init__(self, name, cao):
        self.name = name
        self.cao = cao
        self.dic = {}

    def __str__(self):
        a = []
        a.append(f'Name: {self.name}')
        a.append(f'CAO: {self.cao}')
        a.append(f'Points: {self.point()}')
        return '\n'.join(a)

    def add_grade(self, sub, score):
        self.dic[sub] = score

    def get_grade(self, sub):
        if sub in self.dic:
            return self.dic[sub]
        return 'N/A'

    def point(self):
        grade_table = {
            'H1': 100,
            'H2': 88,
            'H3': 77,
            'H4': 66,
            'H5': 56,
            'H6': 46,
            'H7': 37,
            'H8': 0,
            'O1': 56,
            'O2': 46,
            'O3': 37,
            'O4': 28,
            'O5': 20,
            'O6': 12,
            'O7': 0,
            'O8': 0
        }
        g2p = []
        for g in self.dic.values():
            g2p.append(grade_table[g])
        i = 0
        total = 0
        while i <= 2 and i < len(g2p):
            g2p = sorted(g2p, reverse=True)
            total += g2p[i]
            i += 1
        return total

    def __eq__(self, other):
        return self.point() == other.point()

    def __gt__(self, other):
        return self.point() > other.point()

def main():

    s1 = Student('Boris Spassky', 21345654)
    s2 = Student('Bobby Fischer', 21907321)
    s3 = Student('Mikhail Tal', 21884786)

    s1.add_grade('english', 'H2')
    s1.add_grade('irish', 'H3')
    s1.add_grade('chemistry', 'H5')
    print(s1)

    s2.add_grade('irish', 'H3')
    s2.add_grade('physics', 'H2')
    s2.add_grade('french', 'O1')
    print(s2)

    s3.add_grade('art', 'H1')
    s3.add_grade('music', 'H2')
    s3.add_grade('woodwork', 'H2')
    print(s3)

    assert(s1 == s2)
    assert(s1 < s3)
    assert(s3 > s2)


if __name__ == '__main__':
    main()
