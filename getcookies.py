#! /usr/bin/env python3

import sqlite3 as sql

dbloc = "/home/yiff/.mozilla/firefox/hr7om2sg.default/cookies.sqlite"
dbloc = "bak.sqlite"
con = sql.connect(dbloc)

contents = "host, path, isSecure, expiry, name, value"
f = open("cook.txt", 'w')
for row in con.execute("SELECT "+contents+" FROM moz_cookies;"):
    #print(row)
    f.write("{}\tTRUE\t{}\t{}\t{}\t{}\t{}\n".format(*row))
#file.write(“%stTRUEt%st%st%dt%st%sn” % (row[0], row[1],
#str(bool(row[2])).upper(), row[3], str(row[4]), str(row[5])))
