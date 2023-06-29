# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 20:50:01 2021

@author: lahza
"""


import requests
import re
import urllib.request, urllib.error, urllib.parse
import os
import http.cookiejar
import json
from bs4 import BeautifulSoup
import cv2, wget
from PIL import Image
import imagehash
def get_soup(url,header):
    return BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url,headers=header)),'html.parser');

iquery="brad pitt";Gender='m';startt=0;
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
# with open('codehtmlgoogle3.html', 'w',encoding='utf-8') as fp:
#      fp.write(str(soup))
ActualImages=[]

oneTimeVar=soup.find_all("img")
classname=oneTimeVar[4].get("class")[0]
iiii=soup.find_all("img", {"class":classname})
OringinalSrc=[]

for kkk in iiii:
    actualimagesrc=kkk.get("src")
    ActualImages.append(actualimagesrc)
    tsrc=kkk.parent.parent.get("href")
    src=tsrc[7:tsrc.find("&sa=")]
    OringinalSrc.append(src)
    
from urllib.parse import urlparse
mainImageExtensions=[".webp",".png",".jpg",".jpeg",".jfif",".pjpeg",".pjp",".avif",".apng",".gif"]
mainImageExtensions=[".png",".jpg",".jpeg",".pjpeg",".gif"]
for kkkk in range(0,len(OringinalSrc)):
    image_url = ActualImages[kkkk]
    response = requests.get(image_url)
    file = open("original"+str(kkkk)+'.png', "wb")
    file.write(response.content)
    file.close()
    hashh = imagehash.average_hash(Image.open("original"+str(kkkk)+'.png'))

    kkk=OringinalSrc[kkkk]
    print("original reducted image source is",kkk)
    soup2 = get_soup(kkk,header)
    Allimg=soup2.find_all("img")
    AllSrc=[]
    parsed_uri = urlparse(kkk)
    for kk in Allimg:
        h=kk.get("src")
        if h!=None and h!='':
            AllSrc.append(h)
        
    for kkkkkk in range(len(AllSrc)):
        kk=AllSrc[kkkkkk]
        for k in mainImageExtensions:
            test=False
            if kk.find(k)!=-1:
                if kk[0:2]=='//' or kk[0:4]=='http':
                    if kk[0:2]=='//':
                        kk=parsed_uri.scheme+":"+kk
                    response = requests.get(kk)
                    file = open("originalOo"+str(kkkk)+str(kkkkkk)+k, "wb")
                    file.write(response.content)
                    file.close()
                    Otherhashh = imagehash.average_hash(Image.open("originalOo"+str(kkkk)+str(kkkkkk)+k))
                    test=True
                elif kk[0]=='/' and kk[1]!='/':
                    kk='{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)+kk
                    file = open("originalOo"+str(kkkk)+str(kkkkkk)+k, "wb")
                    file.write(response.content)
                    file.close()
                    test=True
                    Otherhashh = imagehash.average_hash(Image.open("originalOo"+str(kkkk)+str(kkkkkk)+k))
                if test and (Otherhashh-hashh<2):
                    
                    print("original image source is",kk)
                    break
                    
                #finallly=finallly[0:]
                #print(re.search("+.+[/]"+k+"*", kk))
        
    
    
#print("there are total" , len(ActualImages),"images")

# if not(os.path.exists(DIR+'\\'+iquery)):
#             os.mkdir(DIR+'\\'+iquery)
            
# for i , imgsrc in enumerate(ActualImages):
#     try:
#         response = requests.get(imgsrc)
#         file = open(DIR+'\\'+iquery+'\\'+"SmallResGoogle0"+str(i+startt).zfill(3)+iquery+'.png', "wb")
#         file.write(response.content)
#         file.close()
#     except :
#         print("connection error")


# import cv2, wget
# image_url = 'h//upload.wikimedia.org/wikipedia/commons/thumb/d/df/Brad_Pitt_Cannes_2012.jpg/170px-Brad_Pitt_Cannes_2012.jpg'
# filename = wget.download(image_url)
# window = dlib.image_window()
# window.set_image(np_image)
# np_image = cv2.imread(filename)

