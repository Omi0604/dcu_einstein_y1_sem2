#!/usr/bin/env python3

class Student():
    def __init__(self, name, cao):
        self.name = name
        self.cao = cao
        self.d = {}

    def __str__(self):
        a = []
        a.append(f'Name: {self.name}')
        a.append(f'CAO: {self.cao}')
        return '\n'.join(a)

    def add_grade(self, sub, score):
        self.d[sub] = score

    def get_grade(self, sub):
        if sub in self.d:
            return self.d[sub]
        return 'N/A'

class Classlist():
    def __init__(self):
        self.d = {}

    def add(self, student):
        self.d[student.cao] = student

    def remove(self, cao):
        del self.d[cao]

    def lookup(self, cao):
        if cao in self.d:
            return self.d[cao]
        return None

    def __str__(self):
        a = []
        for cao in sorted(self.d):
            a.append(str(self.d[cao]))
        return '\n'.join(a)

    def most_popular_subject(self):
        sub_d = {}
        for student in self.d.values():
            for sub in student.d:
                if sub not in sub_d:
                    sub_d[sub] = 1
                else:
                    count = sub_d[sub]
                    sub_d[sub] = count + 1
        max_sub = max(sub_d.items(), key=sort_on)
        return max_sub[0]

def sort_on(x):
    return x[1]

def main():

    cl = Classlist()
    s1 = Student('Boris Spassky', 21345654)
    s2 = Student('Bobby Fischer', 21907321)
    s3 = Student('Mikhail Tal', 21884786)

    s1.add_grade('english', 'H1')
    s1.add_grade('irish', 'O4')

    s2.add_grade('english', 'H2')
    s2.add_grade('french', 'O5')
    s2.add_grade('spanish', 'O1')

    s3.add_grade('english', 'O3')
    s3.add_grade('irish', 'O3')

    cl.add(s1)
    cl.add(s2)
    cl.add(s3)

    print(cl.most_popular_subject())


if __name__ == '__main__':
    main()
