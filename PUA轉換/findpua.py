#!/usr/bin/env python3

import fileinput
for line in fileinput.input():
  line=line.strip()
  for i in line:
    if 0xE000<=ord(i)<=0xF8FF:
      print(i,"%s:%d"%(fileinput.filename(),fileinput.filelineno()))
