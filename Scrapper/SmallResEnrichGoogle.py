# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 08:16:06 2021

@author: lahza
"""

import requests
import re
import urllib.request, urllib.error, urllib.parse
import os
import http.cookiejar
import json
from bs4 import BeautifulSoup

def get_soup(url,header):
    return BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url,headers=header)),'html.parser')

def SmallresEnrich(iquery="brad pitt",Gender='m',startt=60):
    #r=urllib.request.Request(url,headers=header)# howa request object, r.full_url ,r.get_full_url() ta3tik el lien kaml , 
    #header tosla7 comme quoi el request teb3ath men navigateur ma3rouf
    #header dictionnaire
    #r=urllib.request.urlopen(urllib.request.Request(url,headers=header)).read()
    #query = input("query image")# you can change the query for the image  here
    query= iquery.split();   query='+'.join(query);
    url="https://www.google.com/search?q="+query+"&source=lnms&tbm=isch&start="+str(startt)#+"/search?q=brad+pitt&ie=UTF-8&tbm=isch&ei=szfYYPmmJYa6kwXxi73gCw&start=20&sa=N"
    #add the directory for your image here
    DIR="D:\hajer\Scrapper"
    if Gender=='m':
        DIR=DIR+"\Actors"
    else:
        DIR=DIR+"\Actresses"
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36 "}
    header={'User-Agent':"Chrome/91.0.4472.124"}
    soup = get_soup(url,header)
    # with open('codehtmlgoogle2.txt', 'w',encoding='utf-8') as fp:
    #     fp.write(str(soup))
    ActualImages=[]
    for kkk in soup.find_all("img"):
        if kkk.get("class")[0]=="t0fcAb":
            ActualImages.append(kkk.get("src"))
    #print("there are total" , len(ActualImages),"images")
    
    if not(os.path.exists(DIR+'\\'+iquery)):
                os.mkdir(DIR+'\\'+iquery)
    for i , imgsrc in enumerate(ActualImages):
        try:
            response = requests.get(imgsrc)
            file = open(DIR+'\\'+iquery+'\\'+"SmallResGoogle0"+str(i+startt).zfill(3)+iquery+'.png', "wb")
            file.write(response.content)
            file.close()
        except :
            print("connection error")
SmallresEnrich()
#/search?q=brad+pitt&ie=UTF-8&tbm=isch&ei=szfYYPmmJYa6kwXxi73gCw&start=20&sa=N
# def enrichAll(DIR="D:\hajer\Scrapper"):
#     for kk in os.listdir(DIR+'\Actors'):
#         SmallresEnrich(iquery=kk,Gender='m')
#     for kk in os.listdir(DIR+'\Actresses'):
#         SmallresEnrich(iquery=kk,Gender='f')

# enrichAll(DIR="D:\hajer\Scrapper")

