#! /usr/bin/env python3

import argparse
import sys
import os
import email.parser as parser
import re
import csv

#this script reads the headers of all .eml files in the eml directory and reads out all the ips, creating a .txt list of public ips and a .csv of traces for each email

filepath = 'eml2/'

def getIP(s):
    pattern = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    match = pattern.search(s)
    if match is not None:
        return match.group()
    else:
        return "None"

def processEmail(filepath):
    f = open(filepath, 'rb')
    email = parser.BytesParser().parse(f)
    f.close()
    trace = []
    #data extraction here
    for r in email.get_all("Received"):
        lines = r.split('\n')
        ip = getIP(lines[0])
        trace = [ip] + trace
    return trace

def parseEmails():
    l = []
    for eml in os.listdir(filepath):
        l.append(processEmail(filepath + eml))
    return l

def writeCSV(l):
    with open('data/traces.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        for trace in parseEmails():
            writer.writerow(trace)

def isProperIP(ip):
    p0 = re.compile('127\.\d{1,3}\.\d{1,4}\.\d{1,3}')
    p1 = re.compile('10\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    p2 = re.compile('172\.(1[6-9]|2[0-9]|3[0-1])\.\d{1,3}\.\d{1,3}')
    p3 = re.compile('192\.168\.\d{1,3}\.\d{1,3}')
    if ip is "None":
        return False
    if p0.match(ip) is not None:
        return False
    if p1.match(ip) is not None:
        return False
    if p2.match(ip) is not None:
        return False
    if p3.match(ip) is not None:
        return False
    return True
    
def writeIPList(l):
    s = set()
    for trace in l:
        for ip in trace:
            if isProperIP(ip):
                s.add(ip)
            #else:
                #print("Rejected " + ip)
    ips = open("data/ips.txt", 'w')
    for e in s:
        ips.write(e + '\n')



l = parseEmails()
print(l)
writeCSV(l)
writeIPList(l)


