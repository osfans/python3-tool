#!/usr/bin/python3
import os,datetime,wget,re,sys

path="whb.news365.com.cn/bh"

class bh(wget.wget):
    files="%s/*/*_*.html" % path
    wget_option="http://%s/ -l 0 -A *_*.html" % path
    def getauthor(self):
        return re.findall('</strong><br/>\n(.*?)</td>', self.s, re.S)[0]
    
    def getbody(self):
        return re.findall('width="439" height="1" /></td>.*?(<p>.*?)<p><br /></td>', self.s, re.S)[0]

    def is_need(self, line):
        return '</font></h1>' in line or self.s

    def is_end(self, line):
        return '<p><br /></td>' in line
    
    def entryname(self, name):
        return re.findall("\d{8}",name)[0]

    def parse(self):
        return super(bh, self).parse(encoding="gb18030")

if __name__ == "__main__":
    bh().download()
