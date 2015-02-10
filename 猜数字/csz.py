#!/usr/bin/env python3

import random

n, t = 4, 10
population = range(10)
q = random.sample(population, n)
while q[0] == 0:
    q = random.sample(population, n)
q = "".join(map(str, q))
result = ""

def valid(a):
    return a.isdigit() and len(set(a)) == n

def end(a):
    global result
    r, w = 0, 0
    for j, k in zip(a, q):
        if j == k:
            r += 1
        elif j in q:
            w += 1
    result += "%s：%d正%d歪\n" % (a, r, w)
    end = (r == n)
    print("你猜對了！" if end else result)
    return end

print("""
=======================================
我想了個%d位數，各位互不相同
給你猜%d次，我會告訴你每次猜的結果：
數字和位置都對爲正，數字對但位置不對爲歪
=======================================""" % (n, t))

for i in range(t):
    a = input("第%d次猜：" % (i+1))
    while not valid(a):
        a = input("請重新輸入合法的數字：")
    if end(a):
        break
else:
    print("沒猜出來吧？我想的數字是: %s" % q)
