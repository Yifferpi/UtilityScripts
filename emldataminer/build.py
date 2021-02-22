#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import email.parser as parser
from email import policy
import sys
import os
import re

def parseEmail(filename):
    f = open(filename, 'rb')
    email = parser.BytesParser(policy=policy.default).parse(f)
    f.close()
    line = email.get("From")

    res = re.search("<.*>", line)
    if res is not None:
        print(res.group(0)[1:-1].strip())
    res = re.search("^.*<", line)

    if res is not None:
        tmp = res.group(0)[0:-1]
        res = re.search("\".*\"", tmp)
        if res is not None:
            print(res.group(0)[1:-1].strip())
        else:
            print(tmp.strip())
    print()

    

def main():
    path = sys.argv[1]
    
    for f in os.listdir(path):
        if f.endswith(".eml"):
            parseEmail(path + f)




if __name__ == "__main__":
    main()
