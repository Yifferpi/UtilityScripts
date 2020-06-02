#! /usr/bin/env python3

import argparse
import sys
import os
import email.parser as parser
import re
import csv

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
    for r in email.get_all("Received"):
        lines = r.split('\n')
        ip = getIP(lines[0])
        trace = [ip] + trace
    return trace

with open('egg.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    for eml in os.listdir('eml'):
        print("yey")
        trace = processEmail('eml/' + eml)
        writer.writerow(trace)


#use re (regex) to find domain name and ip address
