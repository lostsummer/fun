#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import collections

Cow = collections.namedtuple('Cow', ['id', 'x', 'y'])
input_file_path = 'connect.in'
output_file_path = 'connect.out'
start_point = Cow(id=0, x=0, y=0)

def readCows(file_path):
    """从输入文件首行个数读入所有奶牛坐标

    :param file_path: 输入文件路径
    :returns : 所有奶牛对象（id，坐标数据）的集合

    """
    cows = set()
    with open(file_path, 'r') as f:
        cow_num = int(f.readline())
        for i in range(cow_num):
            id = i + 1
            l = f.readline()
            x, y = [int(s) for s in l.split()]
            cows.add(Cow(id=id, x=x, y=y))
    return cows


def canMove(cow_c, cow_n):
    """

    :param cow_c: 当前所在奶牛位置
    :param cow_n: 将检查的下一个奶牛位置
    :retruns : 是否可以从 cow_c 移动至 cown_n

    """
    if cow_c.x == cow_n.x or cow_c.y == cow_n.y:
        return True
    else:
        return False

def startMove(start_point, cows):
    """

    :param start_point: 起始位置
    :param cows: 奶牛位置集合
    :return move: 闭包递归函数

    """
    routes = []   # 存入所有的闭环路径
    cow_c = start_point
    cows_r = cows # 未经过奶牛的集合
    ids_past = [] # 按顺序记录走过的位置点id，以将完整闭环存入 routes

    def move():
        """ 闭包内部函数，递归调用，遍历能够返回起始位置的所有路径 """
        nonlocal routes
        nonlocal cow_c
        nonlocal cows_r
        nonlocal ids_past
        # 走至最后一个奶牛，检查是否可回到起始位置
        if len(cows_r) == 0:
            if canMove(cow_c, start_point):
                ids_past.append(cow_c.id)
                ids_past.append(start_point.id)
                routes.append("-".join([str(i) for i in ids_past]))
        else:
            # 逐层遍历，要注意每个节点状态对外层变量的改变只传递给下层，
            # 而不影响同层和上层, 所以要对 list 和 set 深拷贝备份
            cows_r_tmp = cows_r.copy()
            for cow_n in cows_r_tmp:
                if canMove(cow_c, cow_n):
                    cows_r.remove(cow_n)
                    ids_past_tmp = ids_past[:]
                    ids_past.append(cow_c.id)
                    cow_c_cpy = cow_c
                    cow_c = cow_n
                    move()
                    cow_c = cow_c_cpy
                    cows_r = cows_r_tmp.copy()
                    ids_past = ids_past_tmp
        return routes

    return move

def writeOut(num):
    """

    :param num: 写入输出文件的路径数量

    """
    with open(output_file_path, 'w') as f:
        f.write('{}\n'.format(num))

if __name__ == "__main__":
    cows = readCows(input_file_path)
    move = startMove(start_point, cows)
    routes = move()
    routes_num = len(routes)
    print('number of routes: {}'.format(routes_num))
    for r in routes:
        print(r)

    writeOut(routes_num)

