# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 07:21:10 2021

@author: lahza
"""

import requests
from bs4 import BeautifulSoup
import os
import re
import urllib.request#urllib2
import cookielib
import json


def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

query = "brad pitt"
query= query.split()
query='+'.join(query)
url="https://www.google.com/search?q="+query+"&source=lnms&tbm=isch"
r = requests.get(url)

if str(r)=='<Response [200]>':
    soup = BeautifulSoup(r.content, 'html.parser')
    text=soup.find("div", {"class":"bRMDJf islir"})
    text=text.find_all("span", {"class":"itemprop"})