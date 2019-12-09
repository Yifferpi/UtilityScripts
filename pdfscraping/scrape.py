#! /usr/bin/env python3

import argparse
import requests
import bs4
from urllib.parse import urljoin

#=======================================
parser = argparse.ArgumentParser("Scrape all pdfs from a given URL")
parser.add_argument('url', help="URL of the website to scrape")
args = parser.parse_args()

#==========================================

def get_pdflinks():
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
        l = e.get('href')
        if (l is not None) and l.endswith(".pdf"):
            links.append(urljoin(args.url, l))
    return links

def download_pdf(link):
    response = None
    try:
        response = requests.get(link)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
        exit(1)
    name = link.split('/')[-1]
    pdf = open(name, 'wb')
    pdf.write(response.content)
    pdf.close()


links = get_pdflinks()
for i in range(0,5):
    download_pdf(links[i])
