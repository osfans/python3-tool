#!/usr/bin/python3
import os,datetime,wget,re,sys

path="xinmin.news365.com.cn/ygb"

class ygb(wget.wget):
    files="%s/*/*_*.html" % path
    wget_option="http://%s/ -A *_*.html" % path
    def getauthor(self):
        return re.findall('<span class="dwd">(.*?)</span>', self.s, re.S)[0]
    
    def getbody(self):
        return re.findall('<span class="niwuf"><font size="2"> (<div>.*</div><br>)?(.*?)<p></font></span></p>', self.s, re.S)[0][-1]
    
    def is_need(self, line):
        return '<span class="dwd">' in line or '<span class="niwuf">' in line or '<p></font></span></p>' in line

    def is_end(self, line):
        return '<p></font></span></p>' in line
    
    def entryname(self, name):
        return re.findall("\d{8}",name)[0]
    
    def parse(self):
        return super(ygb, self).parse(encoding="gb18030")

if __name__ == "__main__":
    ygb().download()
