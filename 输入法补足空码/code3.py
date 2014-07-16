#!/usr/bin/env python3
from collections import defaultdict

d=defaultdict(list) #记录编码对应的多个汉字
pld=dict()  #记录汉字的字频

for line in open("input.txt"):
    line=line.strip() #去除换行符
    if line:
        hz,bm,pl=line.split("\t")
        d[bm].append(hz)
        pld[hz]=int(pl)

s=set(d.keys())
for bm in s:
    if len(bm)==4 and bm[:3] not in s: #空的三级简码
        d[bm[:3]]=sorted(d[bm[:3]]+d[bm], key=lambda x:-pld[x])[:1] #从全码中选择一个字频最大的汉字

f = open("output.txt","w")
for bm in sorted(d.keys()):
    hz=d[bm]
    if len(bm)>1: hz.sort(key=lambda x:-pld[x]) #重码按字频排序
    if len(bm)==4:
        hz3=d[bm[:3]]
        for i in hz3:
            if i in hz:
                hz.remove(i) #从全码中删除三级简码字
                hz.append(i) #添加到重码的最后
    for i in hz:
        print(i, bm, sep="\t", file = f) #输出所有编码汉字至output.txt
f.close()
