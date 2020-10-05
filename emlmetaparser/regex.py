#! /usr/bin/env python3

d = dict()
d['IP'] = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
d['localIPsmall'] = "192\.168\.\d{1,3}\.\d{1,3}"
d['localIPmedium'] = "172\.(1[6-9]|2[0-9]|3[0-1])\.\d{1,3}\.\d{1,3}"
d['localIPlarge'] = "10\.\d{1,3}\.\d{1,3}\.\d{1,3}"
d['localhost'] = "127\.\d{1,3}\.\d{1,3}\.\d{1,3}"
d['fromtag'] = "^\s*from"
d['bytag'] = "^\s*by"
d['domain'] = "^(?=.{4,255}$)([a-zA-Z0-9][a-zA-Z0-9-]{,61}[a-zA-Z0-9]\.)+[a-zA-Z0-9]{2,5}$"
d['domain1'] = "^(([a-z0-9]\-*[a-z0-9]*){1,63}\.?){1,255}$"
d['domain2'] = "^(?=.{1,255}$)(?!-)[A-Za-z0-9\-]{1,63}(\.[A-Za-z0-9\-]{1,63})*\.?(?<!-)$"


def getRegex(s):
    return d[s]

if __name__ == "__main__":
    main()

