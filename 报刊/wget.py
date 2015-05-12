#!/usr/bin/python3
import os, fileinput, datetime, glob

class wget:
    s=""
    files=""
    wget_option=""

    def download(self):
        os.system("wget -c -k -np -r -l 1 -t 0 %s" % self.wget_option)

    def gettitle(self,title):
        return title

    def getsubtitle(self):
        return ""

    def parse(self, key=None, encoding="U8"):
        files = self.files
        globs = sorted(glob.glob(files), key=key)
        if globs:
            for line in fileinput.input(globs, openhook=fileinput.hook_encoded(encoding)):
                if "<title>" in line:
                    self.s=""
                    title=self.gettitle(line.strip()[7:-8])
                    if not title:
                        self.s=""
                        fileinput.nextfile()
                        continue
                if self.is_need(line):
                    self.s+=line.strip()+"\n"
                    if self.is_end(line):
                        if self.getbody() == "":
                            self.s=""
                            fileinput.nextfile()
                            continue
                        yield title, self.getsubtitle(), self.getauthor(), self.getbody()
                        self.s=""
                        fileinput.nextfile()

