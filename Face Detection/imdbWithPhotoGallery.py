# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 09:10:48 2021

@author: lahza
"""


import requests
from bs4 import BeautifulSoup
import os

s=0 #9999991
def getlinks():
    links=[]
    for i in range(1,10):
        j=str(i)
        while len(j)<7:
            j="0"+j
        j="https://www.imdb.com/name/nm"+j
        links.append(j)
    return links


SaveP="D:\Hajer\Scrapper\\"    ;  filename="ActorsBasicDS.txt" ;FPath=SaveP+filename
urls=getlinks()         #url = "https://www.imdb.com/name/nm0018899/"

if not(os.path.exists(SaveP+"Actors")):
    path = os.path.join(SaveP, "Actors")
    os.mkdir(path)
    
if not(os.path.exists(SaveP+"Actresses")):
    path = os.path.join(SaveP, "Actresses")
    os.mkdir(path)

if not(os.path.exists(SaveP+'ActorsBasicDS.txt')):
    with open(SaveP+'ActorsBasicDS.txt', 'w') as fp:
        fp.write("ActorName"+';'+"Gender"+';"'+"Actor's default image source\"")
        fp.close()
if not(os.path.exists(SaveP+'ActorsNoPhotoDS.txt')):
    with open(SaveP+'ActorsNoPhotoDS.txt', 'w') as fp:
        pass
    
# makes a request to the web page and gets its HTML
for url in urls:
    r = requests.get(url)
    if str(r)=='<Response [200]>':
        soup = BeautifulSoup(r.content, 'html.parser')
        text=soup.find("div", {"class":"infobar"})
        text=text.find_all("span", {"class":"itemprop"})
        for k in text:
            cont=k.get_text()[1:]
            if cont=='Actor' or cont=='Actress':
                s=s+1
                text=soup.find("h1")
                ActorName=text.find_all("span", {"class":"itemprop"})[0].get_text()
                photo=soup.find(id="name-poster")
                if cont=="Actor":
                    path=SaveP+"Actors\\"+ActorName
                    if not(os.path.exists(path)):
                        os.mkdir(path)
                else:
                    path=SaveP+"Actresses\\"+ActorName
                    if not(os.path.exists(path)):
                        os.mkdir(path)
                        
                if photo!=None:         #photo exists
                    photoSrc=photo.get('src')
                    response = requests.get(photoSrc)
                    if cont=="Actor":
                        file = open(path+'\\'+str(ActorName)+'.png', "wb")
                        file.write(response.content)
                        file.close()
                        
                        f = open(SaveP+'ActorsBasicDS.txt', 'a')
                        f.write('\n'+ActorName+';'+'m'+';"'+photoSrc+'\"')
                        f.close()           
                        
                    else:
                        file = open(path+'\\'+str(ActorName)+'.png', "wb")
                        file.write(response.content)
                        file.close()
                        f = open(SaveP+'ActorsBasicDS.txt', 'a')
                        f.write('\n'+ActorName+';'+'f'+';"'+photoSrc+'\"')
                        f.close()    
                    ########################################################################################
                    #rEnrich = requests.get(url)
                    
                    
                    ########################################################################################
                else:
                    f = open(SaveP+'ActorsNoPhotoDS.txt', 'a')
                    f.write('\n'+ActorName)
                    f.close()
                    if cont=="Actor":
                        f = open(SaveP+'ActorsBasicDS.txt', 'a')
                        f.write('\n'+ActorName+';'+'m'+';'+'-')
                        f.close()
                    else:
                        f = open(SaveP+'ActorsBasicDS.txt', 'a')
                        f.write('\n'+ActorName+';'+'m'+';'+'-')
                        f.close()                        


