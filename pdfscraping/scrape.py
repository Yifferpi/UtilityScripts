#! /usr/bin/env python3

import argparse
import requests
import bs4
from urllib.parse import urljoin
from getpass import getpass

#=======================================
parser = argparse.ArgumentParser("Scrape all pdfs from a given URL")
parser.add_argument('url', help="URL of the website to scrape")
parser.add_argument('-i', '--interactive', action='store_true', help="Use Credentials interactive")
parser.add_argument('-k', '--keyword', help="Only fetch pdfs with this keyword in its name")
parser.add_argument('-a', '--available', action='store_true', help="Only list all pdfs that would be downloaded")
args = parser.parse_args()

#==========================================

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

def filter_links(links):
    links = [x for x in links if (x is not None) and x.endswith(".pdf")]
    if args.keyword is not None:
        links = [x for x in links if args.keyword in x.split('/')[-1]]
    return links

def print_links(links):
    print("Found " + str(len(links)) + " pdf files:")
    for l in links:
        print(l.split('/')[-1])

#Something buggy here... ValueError in reqest.get(l, cred)
def download_links(links, cred=None):
    numSucc = 0
    for l in links:
        r = None
        try:
            if cred is None:
                r = requests.get(l)
            else:
                r = requests.get(l, cred)
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
            if response.status_code == requests.codes.unauthorized:
                print("Use the -i flag for interactive credentials")
            continue
        numSucc = numSucc + 1
        name = l.split('/')[-1]
        pdf = open(name, 'wb')
        pdf.write(r.content)
        pdf.close()
    return numSucc

#Get credentials if required
cred = None
if args.interactive:
    user = input("Username: ")
    passwd = getpass()
    cred = (user, passwd)

links = filter_links(get_links())

if args.available:
    print_links(links)
else:
    n = download_links(links, cred)
    print("Successful downloads: " + str(n) + " out of " + str(len(links)))

