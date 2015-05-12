#!/usr/bin/python3
import os,datetime,wget,re, urllib.request,sys

t=datetime.date.today()
path="paper.people.com.cn/rmrb/html"

class rmrb(wget.wget):
    files="%s/*/*/*-*.htm"%path

    def getsubtitle(self):
        return re.findall('<h2>(.*?)</h2>', self.s, re.S)[0]

    def getauthor(self):
        return re.findall('<div class="lai"  style="padding-top:5px;">(.*?)</div>', self.s, re.S)[0].replace("\n","")
    
    def getbody(self):
        return re.findall('<!--enpcontent-->(.*?)<!--/enpcontent-->', self.s, re.S)[0].strip("<P></P>")

    def is_need(self, line):
        return self.s or '<h2>' in line

    def is_end(self, line):
        return "<!--/enpcontent-->" in line
    
    def entryname(self, name):
        return re.findall("\d{8}_\d+",name)[0]

if __name__ == "__main__":
    s = urllib.request.urlopen("http://%s/%04d-%02d/%02d/nbs.D110000renmrb_01.htm" % (path,t.year,t.month,t.day)).read().decode("U8")
    name = re.findall('<div class="right_title-name"><a id=pageLink href=.*?>第(.*?)版：副刊</a></div>', s)
    num=int(name[0])
    a=rmrb()
    a.wget_option="http://%s/%04d-%02d/%02d/nbs.D110000renmrb_%02d.htm -A *-%02d.htm" % (path,t.year,t.month,t.day,num,num)
    a.download()
