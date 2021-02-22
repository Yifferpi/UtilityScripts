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
    
    name, mail = ("", "")

    res = re.search("^.*<", line)
    if res is not None:
        tmp = res.group(0)[0:-1]
        res = re.search("\".*\"", tmp)
        if res is not None:
            name = res.group(0)[1:-1].strip()
        else:
            name = tmp.strip()

    res = re.search("<.*>", line)
    if res is not None:
        mail = res.group(0)[1:-1].strip()

    return (name, mail)

def printList(l):
    for e in l:
        print("{:30.30}{}".format(*e))

def main():
    path = sys.argv[1]
    l = list()    
    for f in os.listdir(path):
        if f.endswith(".eml"):
            l.append(parseEmail(path + f))
    x = len(l) 
    l = list(set(l))
    y = len(l)
    printList(l)
    print(x)
    print(y)


if __name__ == "__main__":
    main()
