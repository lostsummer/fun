#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections

Point = collections.namedtuple('Point', ['id', 'x', 'y'])

input_file_path = 'connect.in'
output_file_path = 'connect.out'
start = Point(id=0, x=0, y=0)

def readCows():
    with open(input_file_path, 'r') as f:
        return {Point(i+1, *[int(s) for s in f.readline().split()]) for i in range(int(f.readline()))}

def walkRound(rest, past=[start.id], c=start):
    connectable = lambda n: c.x == n.x or c.y == n.y
    moveto = lambda n: (rest.difference([n]), past + [n.id])
    if not rest and connectable(start):
        yield ' -> '.join([str(i) for i in past + [start.id]])
    for n in filter(connectable, rest):
        yield from walkRound(*moveto(n), n)

def writeOut(num):
    with open(output_file_path, 'w') as f:
        f.write('{}\n'.format(num))

if __name__ == "__main__":
    routes = [r for r in walkRound(readCows())]
    num = len(routes)
    writeOut(num)
    print("number of routes: {}".format(num))
    [print(r) for r in routes]
