#! /usr/bin/env python3

#take list of ips as txt, look them up and write resulting data in json
import ipinfo
import csv


fn = ['ip','host','city','region','country','lat','long','postal','tz']

#returns a dictionary whose keys are the ips and values are dictionaries containing all the info
def loadDB():
    data = open('data/data.csv', 'r')
    reader = csv.DictReader(data)
    db = dict()
    for row in reader:
        db[row['ip']] = row
    return db

def storeDB(db):
    data = open('data/data.csv', 'w')
    writer = csv.DictWriter(data, fieldnames=fn)
    writer.writeheader()
    for ip in db.keys():
        writer.writerow(db[ip])

def loadNew(db):
    #load new only if not known already
    source = open('data/ips.txt','r')
    l = source.read().split('\n')
    l = list(set(l))
    return [i for i in l if not i in db and not i == '']

def getHandler():
    access_token = '3bf84f429176a4'
    handler = ipinfo.getHandler(access_token)
    return handler

#fn = ['ip','host','city','region','country','lat','long','postal','tz']
def getInfo(ip, handler):
    details = handler.getDetails(ip)
    row = dict()
    row['ip'] = details.ip
    row['host'] = details.hostname
    row['city'] = details.city
    row['region'] = details.region
    row['country'] = details.country
    latlon = details.loc.split(',')
    row['lat'] = latlon[0] 
    row['long'] = latlon[1]
    row['postal'] = details.postal
    row['tz'] = details.timezone
    return row

db = loadDB()
l = loadNew(db)
h = getHandler()
for ip in l:
    row = getInfo(ip, h)
    db[row['ip']] = row
print("Retrieved " + str(len(l)) + " entries")
storeDB(db)
