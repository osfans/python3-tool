#!/usr/bin/env python3
import importlib, datetime

t = datetime.date.today()
fname = "%s.htm" % t
cname={"bh":"笔会", "rmrb":"人民日报", "ygb":"夜光杯", "bdzk":"冰点周刊"}

fmt = """<h2><a name="%s">%s</a></h2><div id=s>%s</div><div id=a>%s</div>
<div id=b>%s</div>
<mbp:pagebreak/>
"""

titlefmt = "t%d"

ddd = []
body = []
count=0
for name in sorted(cname.keys()):
    #body.append("""<h1 id=paper>%s</h1>"""%(cname[name]))
    a=getattr(importlib.import_module(name), name)
    for i in a().parse():
        title=titlefmt % count
        body.append(fmt%((title,)+i))
        ddd.append(i[0])
        count+=1

f = open(fname, "w")
print("""<html>
<head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></head>
<body>
<a name="start"><h1>致maomao☺</h1></a>
<p>制作人：老公</p>
<p>制作时间：%s</p>
<mbp:pagebreak/>

<p><a name="TOC"><h1>目录</h1></a></p>
""" % t, file=f)

for i in range(len(ddd)):
    title=titlefmt % i
    print('<p><a href="#%s">%s</a></p>' % (title,ddd[i]), file=f)
print("<mbp:pagebreak/>", file = f)

for line in body:
    print(line, file=f)

print("</body></html>", file = f)
f.close()
