#!/usr/bin/env python3
import sys

if len(sys.argv) == 1:
  print("Usage: %s filename" % sys.argv[0])
  exit

cnpua="""
	⺁	𠂆
	𠂇
	𠂉
	𠃌
	⺄
	㑳
	㑇
	⺈	𠂊
	⺋	㔾
	龴
	㖞
	㘚
	㘎
	⺌
	⺗	㣺
	㥮
	㤘
	龵
	㧏
	㧟
	㩳
	㧐
	龶
	龷
	㭎
	㱮
	㳠
	⺧	𠂒
	𡗗
	龸
	⺪	𤴔
	䁖
	䅟
	⺮	𥫗
	䌷
	⺳	㓁
	⺶
	⺷	𦍌
	𢦏
	䎱
	䎬
	⺻
	䏝
	䓖
	䙡
	䙌
	龹
	䜣
	䜩
	䝼
	䞍
	⻊	𧾷
	䥇
	䥺
	䥽
	䦂
	䦃
	䦅
	䦆
	䦟
	䦛
	䦷
	䦶
	龺
	𤇾
	䲣
	䲟
	䲠
	䲡
	䱷
	䲢
	䴓
	䴔
	䴕
	䴖
	䴗
	䴘
	䴙
	䶮
	龻
"""

pua_dict = {}
for line in cnpua.strip().split("\n"):
  fs = line.split("\t")
  pua_dict[fs[0]]=fs[-1]

tr = str.maketrans(pua_dict)

for fn in sys.argv[1:]:
  s = ""
  f = open(fn, "r")
  for line in f:
    s+=line.translate(tr)
  f.close()
  t = open(fn, "w")
  t.write(s)
  t.close()
