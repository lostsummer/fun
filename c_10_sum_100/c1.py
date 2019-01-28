#!/usr/bin/env python3

BIGGEST = 100 - sum(range(1, 10))

def fetch(current=0, selected=[]):
    if current <= BIGGEST and len(selected) < 10:
        if current > 0:
            selected_ = selected + [current]
        else:
            selected_ = selected + []
        sum_val = sum(selected_)
        n = len(selected_)
        if sum_val == 100 and n == 10:
            yield selected_
        elif sum_val < 100 and n < 10:
            for i in range(current+1, 100 - sum_val + 1):
                yield from fetch(i, selected_)

choices = [i for i in fetch(0)]
#print("number of choices: {}".format(len(choices)))
for i in choices:
    print(','.join([str(i) for i in i]))
