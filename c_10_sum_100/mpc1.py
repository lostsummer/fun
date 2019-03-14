#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import itertools
from multiprocessing import Pool

"""
算法有3个重要的优化点:
    1. 组合中的最大元素BIGGEST有限制，也就是考虑前9个数和最小的情况
    2. 组合按生序排列的首元素有最大限制，首元素是我们递归试算的起始点
    3. 待选元素范围从已选最大值+1到100-已选原色之和
"""

BIGGEST = 100 - sum(range(1, 10))
MAX_HEAD = list(itertools.takewhile(lambda x:sum(x)<=100, (range(1, 101)[i:i+10] for i in range(0, 100))))[-1][0]

def fetch(current, selected=[]):
    if current <= BIGGEST:
        selected_ = selected + [current]
        sum_val = sum(selected_)
        n = len(selected_)
        if sum_val == 100 and n == 10:
            yield selected_
        elif sum_val < 100 and n < 10:
            for i in range(current+1, 100-sum_val+1):
                yield from fetch(i, selected_)

def work(start):
    return [i for i in fetch(start)]

if __name__ == '__main__':
    pool = Pool(MAX_HEAD)
    results = pool.map(work, range(1, MAX_HEAD+1))
    pool.close()
    pool.join()
    for r in results:
        for c in r:
            print(','.join(str(i) for i in c))
