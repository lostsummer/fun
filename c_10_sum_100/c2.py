#!/usr/bin/env python

def get_combs(n=100, k=10, tg=100):
    combs = []
    x = tg - sum(range(1, k))

    def dfs(comb, idx=0, k=k, t=tg):
        #dmx = min(tg - sum(comb), x, n)
        dmx = min(tg - sum(comb), x, n)
        arr = range(1, dmx + 1)
        if t == 0 and k == 0:
            combs.append(comb[:])
            return
        if dmx <= idx or k < 0 or t < 0:
            return
        for i in range(idx, dmx):
            v = arr[i]
            dfs(comb + [v], i + 1, k - 1, t - v)

    dfs([])

    return combs

result = get_combs()
for i in result:
    print(','.join([str(j) for j in i]))
