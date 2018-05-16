#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import collections

INPUT_FILE_PATH = 'connect.in'
OUTPUT_FILE_PATH = 'connect.out'

Point = collections.namedtuple('Point', ['id', 'x', 'y'])
start = Point(id=0, x=0, y=0)

def readCows():
    """从输入文件首行个数读入所有奶牛坐标

    :param file_path: 输入文件路径
    :returns : 所有奶牛对象（id，坐标数据）的集合

    """
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
    """

    :param rest: 除却当前点以外未经过点的集合
    :param c: 当前点
    :param past: 经过点顺序列表用来记录路径
    :yield : 形成闭环的路径

    """
    isConnectable = lambda c, n: c.x == n.x or c.y == n.y
    toPoint = lambda rest, past, n: (rest.difference(set([n])), past + [n.id])

    # 逐层遍历，要注意每个节点状态对外层变量的改变只传递给下层，
    # 而不影响同层和上层, 所以要对rest拷贝，past还原.
    for n in rest:
        if isConnectable(c, n):
            yield from walkRound(*toPoint(rest, past, n), n)
    if len(rest) == 0:
        if isConnectable(c, start):
            past_n = past + [start.id]
            route = '-'.join([str(i) for i in past_n])
            yield route

def writeOut(num):
    """

    :param num: 写入输出文件的路径数量

    """
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

