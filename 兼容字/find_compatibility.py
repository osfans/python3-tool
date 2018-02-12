#!/usr/bin/env python3
"""查找文件中使用的兼容字"""

import fileinput
for line in fileinput.input():
    line = line.strip()
    for i in line:
        order = ord(i)
        if 0xF900 <= order < 0xFB00 \
        and i not in '﨎﨏﨑﨓﨔﨟﨡﨣﨤﨧﨨﨩' \
        or 0x2F800 <= order < 0x2FA20:
            print("\033[35m%s\033[00m:\033[32m%d\033[00m\t%s" % \
            (fileinput.filename(), \
            fileinput.filelineno(), \
            line.replace(i, "\033[91m\033[01m{}\033[00m".format(i))))
