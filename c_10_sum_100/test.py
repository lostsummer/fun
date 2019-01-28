#!/usr/bin/env python

import sys

def travel_result(filename, func):
    allpass = True
    with open(filename, 'r') as f:
        for line in f:
            success, msg = func(line)
            if not success:
                print(msg)
                allpass = False
    return allpass

def check_sum(line):
    numbers = [int(i) for i in line.split(',')]
    sum_v = sum(numbers)
    if sum_v == 100 and len(numbers) == 10:
        return True, ''
    else:
        return False, 'error! line: {l}, sum: {s}'.format(l=line, s=sum_v)

choices = []
def check_uniq(line):
    global choices
    c = {int(i) for i in line.split(',')}
    if len(c) != 10:
        return False, '"{l}" has not 10 uniq number'.format(line)
    elif c in choices:
        return False, '{c} repeated'.format(c)
    else:
        choices.append(c)
        return True, ''

filename = sys.argv[1]
if travel_result(filename, check_sum):
    print("Pass check sum test")
else:
    print("Not pass check sum test")

if travel_result(filename, check_uniq):
    print("Pass check uniq test")
else:
    print("Not pass check uniq test")
