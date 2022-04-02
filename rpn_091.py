#!usr/bin/env python3
from math import sqrt


class Stack():
    def __init__(self):
        self.ls = []

    def push(self, e):
        self.ls.append(e)

    def pop(self):
        return self.ls.pop()

    def top(self):
        return self.ls[-1]

    def is_empty(self):
        return len(self.ls) == 0

    def __len__(self):
        return len(self.ls)


def is_float(a_string):
    try:
        float(a_string)
        return True
    except ValueError:
        return False


def calculator(s):
    binops = {'+': float.__add__, '-': float.__sub__,
              '*': float.__mul__, '/': float.__truediv__}

    uniops = {'n': float.__neg__, 'r': sqrt}

    rpn = Stack()
    for token in s.split():
        if is_float(token):
            rpn.push(float(token))
        else:
            if token in binops:
                n1 = rpn.pop()
                n2 = rpn.pop()
                result = binops[token](n2, n1)
                rpn.push(result)

            if token in uniops:
                n = rpn.pop()
                result = uniops[token](n)
                rpn.push(result)
    return rpn.top()
