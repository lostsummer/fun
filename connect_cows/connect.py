#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import collections

Point = collections.namedtuple('Point', ['id', 'x', 'y'])

INPUT_FILE_PATH = 'connect.in'
OUTPUT_FILE_PATH = 'connect.out'

start = Point(id=0, x=0, y=0)

def readCows():
    cows = set()
    with open(INPUT_FILE_PATH, 'r') as f:
        cow_num = int(f.readline())
        for i in range(cow_num):
            id = i + 1
            l = f.readline()
            x, y = [int(s) for s in l.split()]
            cows.add(Point(id=id, x=x, y=y))
    return cows


def walkRound(rest, past=[start.id], c=start):
    isConnectable = lambda n: c.x == n.x or c.y == n.y
    toPoint = lambda n: (rest.difference(set([n])), past + [n.id])
    for n in rest:
        if isConnectable(n):
            yield from walkRound(*toPoint(n), n)
    if len(rest) == 0:
        if isConnectable(start):
            past_n = past + [start.id]
            route = '-'.join([str(i) for i in past_n])
            yield route

def writeOut(num):
    with open(OUTPUT_FILE_PATH, 'w') as f:
        f.write('{}\n'.format(num))

if __name__ == "__main__":
    cows = readCows()
    routes = [r for r in walkRound(cows)]
    num = len(routes)
    writeOut(num)
    print("number of routes: {}".format(num))
    for r in routes:
        print(r)

