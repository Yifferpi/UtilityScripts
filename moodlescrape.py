#! /usr/bin/env python3

import requests
from bs4 import BeautifulSoup


baseurl = "https://moodle.ethz.ch"

auth = {
        'action': 'login',
        'username': 'basilo',
        'password': 'Aladin@bo.2018'
        }

loginurl = baseurl + 'login/index.php'
ses = Session()
r = ses.post(loginurl, data=auth)

print(r.status_code)
