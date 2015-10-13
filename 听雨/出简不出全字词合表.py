#!/usr/bin/env python3
from collections import defaultdict

#字頻表
zp=defaultdict(int)
for i in open("字频.txt",encoding="U16"):
  i = i.strip()
  if i:
    z,p=i.split("\t")
    zp[z]=int(p)

#原始字表
zm = defaultdict(list)
for i in open("原始码字.txt", encoding="U16"):
  i = i.strip()
  if i:
    z,m = i.split()
    zm[z].append(m)

#詞頻
phrases = list()
for i in open("词频.txt", encoding="U16"):
  i = i.strip()
  if i:
    c,p = i.split()
    if len(c)> 1 :
      phrases.append(c)
phraseset = set(phrases)

#詞表
for i in open("词表.txt", encoding="U16"):
  i = i.strip()
  if i:
    phrase = i.split()[0]
    if phrase not in phraseset: phrases.append(phrase)

f = open("出简不出全字词合表.txt", "w", encoding="U16")
codes=set()
for z in sorted(zm.keys(), key=lambda z:zp[z],reverse=True):
  for y in zm[z]:
    for i in range(3,5):
      if len(y)>i and y[:i] not in codes:
        y=y[:i] #首字簡碼
      #else:
        #y=y[:4]
    codes.add(y)
    print("%s\t%s"%(z,y),file=f)#print("%s\t%s%d"%(z,y,zp['']),file=f）

#f = open("出简不出全字词合表.txt", "w", encoding="U16")
codes=set()
for z in sorted(zm.keys(), key=lambda z:zp[z],reverse=True):
  for y in zm[z]:
    for i in range(3,5):
      if len(y)>i:# and y[:i] not in codes:
        y=y[:i] #首字簡碼
    #if len(y) == 4 and zp[z] == 0: y = "" #四碼〇頻字加q
    #if len(y) == 4 and zp[z] == 0: y = "e" #四碼〇頻字加q
    #codes.add(y)
    print("%s\t%s"%(z,y),file=f)#print("%s\t%s%d"%(z,y,zp['']),file=f）

for s in phrases:
  l = len(s)
  try:
    if l == 1: continue
    elif l == 2:
      code = zm[s[0]][0][:2]# + zm[s[1]][0][0]
      if code in codes: code += zm[s[1]][0][0]
      #if code in codes: code += zm[s[-1]][0][0]
      if code in codes: continue
    #elif l == 3:
      #code = zm[s[0]][0][0] + zm[s[1]][0][0]# + zm[s[2]][0][0]
      #if code in codes: code+='q'
      #if code in codes: code += zm[s[2]][0][0]
      #if code in codes: code += zm[s[3]][0][3]
      #if code in codes: continue
    #elif l == 4:
      #code = zm[s[0]][0][:2] + zm[s[1]][0][0] + zm[s[2]][0][0] + zm[s[3]][0][0]
      #if code in codes: code+='m'
      #if code in codes: code += zm[s[3]][0][1]
    else:
      code = zm[s[0]][0][0] + zm[s[1]][0][0]# + zm[s[-1]][0][0]
      #if code in codes: code+='q'
      if code in codes: code += zm[s[2]][0][0]
      #if code in codes: code += zm[s[1]][0][0] + zm[s[-1]][0][3]
      #if code in codes: code += zm[s[-1]][0][4]
      #if len(code) == 4 and code in codes: code+='m' #四碼重碼詞加q
      #if len(code) == 5 and code in codes: code+=code[-1] #五碼重碼詞雙寫末碼
      if code in codes: continue
    codes.add(code)
    print("%s\t%s" % (s, code), file = f)
  except:
    pass
f.close()
