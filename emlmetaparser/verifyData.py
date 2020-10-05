#! /usr/bin/env python3

import regex as rx
import parseEmail as pe
import email.parser as parser
import re
import os

filepath = 'eml2/'

def loadEmails():
    l = list()
    for email in os.listdir(filepath):
        f = open(filepath + email, 'rb')
        content = parser.BytesParser().parse(f)
        f.close()
        l.append(pe.parseEmail(content))
    return l

def printDict(d):
    for e in d:
        print("NewMail")
        for i in e['fromtrace']:
            print(i)
        print()
        for i in e['bytrace']:
            print(i)
        print("==========================")

def printLists(l1, l2):
    print("New Mail")
    for a, b in zip(l1, l2):
        print(a)
        print(b)
        print()
    print("==============")

def filterIPs(oldList):
    pattern = re.compile(rx.getRegex("domain1"))
    newList = []
    for i in oldList:
        if pattern.search(i) is not None:
            newList.append(pattern.search(i).group())
        else:
            newList.append(i)
    return newList

def filterDict(dictList):
    for d in dictList:
        fromList = d['fromtrace']
        byList = d['bytrace']
        fromList2 = filterIPs(fromList)
        byList2 = filterIPs(byList)
        printLists(fromList, fromList2)
        d['fromtrace'] = fromList2
        d['bytrace'] = byList2


    

def main():
    emailList = loadEmails()
    #printDict(emailList)
    filterDict(emailList)
    #printDict(emailList)

if __name__ == "__main__":
    main()


