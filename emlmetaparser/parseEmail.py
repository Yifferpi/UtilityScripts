#! /usr/bin/env python3

import email.parser as parser
import re
import regex as rx

#this script reads an email and prints sender receiver and subject
#the parseEmail function is of interest

def findStr(expr, received):
    sublist = received.split('\n')
    res = "#"
    pattern = re.compile(expr) 
    for line in sublist:
        if pattern.search(line) is not None: 
            res = line
    return res

def parseEmail(e):
    d = dict()
    d['sender'] = e.get("From")
    d['receiver'] = e.get("Delivered-To")
    d['subject'] = e.get("Subject")
    receivedList = e.get_all("Received")
    fromList = list()
    byList = list()
    for received in receivedList:
        fromList.append(findStr(rx.getRegex("fromtag"), received))
        byList.append(findStr(rx.getRegex("bytag"), received))
    d['fromtrace'] = fromList
    d['bytrace'] = byList
    return d

def main():
    filepath = 'eml2/1.eml'
    f = open(filepath, 'rb')
    email = parser.BytesParser().parse(f)
    f.close()
    d = parseEmail(email)
    print(d['sender'])
    print(d['receiver'])
    print(d['Subject'])

if __name__ == "__main__":
    main()
