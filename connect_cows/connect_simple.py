#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 偷懒没写输入，只把题目示例当做测测试数据
# 用了很多全局变量不优雅
# 递归层次太深可能会爆栈

start = (0, 0)
p1 = (0, 1)
p2 = (2, 1)
p3 = (2, 0)
p4 = (2, -5)


restcows = {p1, p2, p3, p4}

routenum = 0

# c: current point
# n: next point
def check(c, n):
    if c[0] != n[0] and c[1] != n[1]:
        return False
    else:
        return True

# c: current point
# rs: set of rest points
def move(c, rs):
    if len(rs) == 0:
        if check(c, start):
            global routenum
            routenum += 1
            return
    else:
        for n in rs:
            if check(c, n):
                rs_n = rs.copy()
                rs_n.remove(n)
                move(n, rs_n)


if __name__ == "__main__":
    move(start, restcows)
    print(routenum)
