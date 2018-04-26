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


def isConnectable(c, n):
    """

    :param c: 当前所在奶牛位置
    :param n: 将检查的下一个奶牛位置
    :retruns : 是否可以从 c 移动至 n

    """
    if c.x == n.x or c.y == n.y:
        return True
    else:
        return False


def walkRound(left, c=start, past=[start.id]):
    """

    :param left: 除却当前点以外未经过点的集合
    :param c: 当前点
    :param past: 经过点顺序列表用来记录路径
    :yield : 形成闭环的路径

    """
    # 逐层遍历，要注意每个节点状态对外层变量的改变只传递给下层，
    # 而不影响同层和上层, 所以要对left拷贝，past还原.
    for n in left:
        if isConnectable(c, n):
            left_n = left.copy()
            left_n.remove(n)
            past_n = past[:]
            past_n.append(n.id)
            yield from walkRound(left_n, n, past_n)
    if len(left) == 0:
        if isConnectable(c, start):
            past_n = past[:]
            past_n.append(start.id)
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

