#!/usr/bin/env python3

import random

p = ['龙王', '神龙', '金龙', '青龙', '赤龙', '白龙', '风雨龙', '变形龙', '虎王', '东北虎', '大头虎', '下山虎', '绿虎', '妖虎', '白虎', '小王虎']
d = list(range(1, 17))
pd = dict(zip(p, d))
dp = dict(zip(d, p))
n = len(p) // 2
random.shuffle(d)
a = d[:n]
b = d[n:]

def have():
    for i in sorted(a):
        print("%2d: %s" % (i, dp[i]))
    return a

def valid(i):
    if i.isdigit():
        i = int(i)
        if i in a:
            a.remove(i)
            return i

def end():
    if set(a)>={1,16} or set(a)>=set(range(9,17)):
        print("赢了!")
        return True
    elif set(b)>={1,16} or set(b)>=set(range(9,17)):
        print("输了!")
        return True

def check(i):
    random.shuffle(b)
    j = b.pop()
    l = [i, j]
    if (i == 16 and j <= 8) or (j==16 and i > 8) or (j != 16 and i < j):
        print("%s > %s" % (dp[i], dp[j]))
        a.extend(l)
    else:
        print("%s < %s" % (dp[i], dp[j]))
        b.extend(l)

while have():
    if end():
        break
    i = valid(input("請出牌:"))
    while not i:
        i = valid(input("請重新出牌:"))
    check(i)

