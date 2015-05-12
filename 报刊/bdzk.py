#!/usr/bin/python3
import os,datetime,wget,re,sys

path="zqb.cyol.com/html"

t=datetime.date.today()

urls=[]
for i in range(9,13):
    url="http://%s/%04d-%02d/%02d/nbs.D110000zgqnb_%02d.htm" % (path,t.year,t.month,t.day,i)
    urls.append(url)

class bdzk(wget.wget):
    files="%s/*/*/*-*.htm"%path
    wget_option=" ".join(urls) + ' -A "*-*.htm"'
    def gettitle(self, title):
        return title[:-6]

    def getsubtitle(self):
        return re.findall('<h2>(.*?)</h2>', self.s, re.S)[0]

    def getauthor(self):
        return re.findall('<div class="lai">(.*?)</div>', self.s, re.S)[0].replace("\n","")
    
    def getbody(self):
        return re.findall('<!--enpcontent-->(.*?)<!--/enpcontent-->', self.s, re.S)[0]

    def is_need(self, line):
        return self.s or '<h2>' in line

    def is_end(self, line):
        ret = "<!--/enpcontent-->" in line
        if ret: self.s=re.sub('\n+<div class="c_c BSHARE_POP">.*</script>\n+',"\n",self.s, flags=re.S)
        return ret
    
    def entryname(self, name):
        return re.findall("\d{8}_\d+-\d{2}",name)[0]

    def parse(self):
        return super(bdzk, self).parse(key=lambda x:x[-6:-4]+x[16:-7])

if __name__ == "__main__":
    bdzk().download()
