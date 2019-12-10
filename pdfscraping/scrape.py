#! /usr/bin/env python3

import argparse
import requests
import bs4
import os
import datetime
import pytz
from dateutil.parser import parse
from urllib.parse import urljoin
from getpass import getpass

#=======Arguments================================
parser = argparse.ArgumentParser("Scrape all pdfs from a given URL")
parser.add_argument('url', help="URL of the website to scrape")
parser.add_argument('-i', '--interactive', action='store_true', help="Use Credentials interactive")
parser.add_argument('-k', '--keyword', help="Only fetch pdfs with this keyword in its name")
parser.add_argument('-a', '--available', action='store_true', help="Only list all pdfs that would be downloaded")
args = parser.parse_args()

#=======Acquire and filter===================================

def get_links():
    links = []
    response = None
    try:
        response = requests.get(args.url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
        exit(1)
    soup = bs4.BeautifulSoup(response.content, 'html.parser')
    for e in soup.find_all('a'):
        links.append(urljoin(args.url, e.get('href')))
    return links

def pdffilter(links):
    tmp = [x for x in links if (x is not None) and x.endswith(".pdf")]
    if args.keyword is not None:
        tmp = [x for x in tmp if args.keyword in x.split('/')[-1]]
    return tmp

def updatablefilter(links):
    return [x for x in links if nonexistent_or_updatable(x)]

def nonexistent_or_updatable(linktofile):
    filename = linktofile.split('/')[-1]
    if os.path.isfile(filename):

        filetime = datetime.datetime.fromtimestamp(os.path.getmtime(filename))
        zone = pytz.timezone('Europe/Zurich')
        filetime = zone.localize(filetime)
        r = None
        try:
            if cred is None:
                r = requests.head(linktofile)
            else:
                r = requests.head(linktofile, auth=cred)
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
            return False
        urltime = parse(r.headers['Last-Modified'])

        if urltime < filetime:
            print(filename + " already exists and is up-to-date")
            return False
    return True






#=======Print or download======================================

def print_links(links):
    print("Found " + str(len(links)) + " pdf files:")
    for l in links:
        print(l.split('/')[-1])

def download_links(links):
    links = updatablefilter(links)
    numSucc = 0
    for l in links:
        filename = l.split('/')[-1]
        content = None
        try:
            content = download_file(l, cred)
        except requests.exceptions.HTTPError as err:
            print(err)
            print(filename + " could not be downloaded")
            continue
        numSucc = numSucc + 1

        print("Successfully downloaded " + filename)
        pdf = open(filename, 'wb')
        pdf.write(content)
        pdf.close()

    print("Successful downloads: " + str(numSucc) + " out of " + str(len(links)))
    return numSucc

def download_file(link, cred = None):
    r = None
    if cred is None:
        r = requests.get(link)
    else:
        r = requests.get(link, auth=cred)
    r.raise_for_status()
    return r.content



#=======Main====================================================
#Global
cred = None
if args.interactive:
    user = input("Username: ")
    passwd = getpass()
    cred = (user, passwd)

links_all = get_links()
links_onlypdf = pdffilter(links_all)

if args.available:
    print_links(links_onlypdf)
else:
    download_links(links_onlypdf)


