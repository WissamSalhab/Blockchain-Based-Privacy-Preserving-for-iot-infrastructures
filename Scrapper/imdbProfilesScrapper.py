# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 16:23:10 2021

@author: hajerBouani
"""

import requests
from bs4 import BeautifulSoup
import os
f = open("imdbProgress.txt", "r")
reached=int(f.read()) #9999991
f.close()
lastAct=reached
currentnetwork=0
def getlinks():
    links=[]
    global reached
    for i in range(reached,4500):
        j=str(i)
        while len(j)<7:
            j="0"+j
        j="https://www.imdb.com/name/nm"+j
        links.append(j)
    return links
def reconnectWiFINetwork(namesssids):
    import subprocess
    global currentnetwork
    import time
    command ="netsh wlan disconnect interface=\"Wi-Fi\""
    result = os.popen(command)
    command = """netsh wlan connect ssid=\"{}\" name=\"{}\""""
    test=False
    iterati=0
    while ((iterati<2*len(namesssids)) and (not test)):
        iterati=iterati+1
        currentnetwork=currentnetwork+1
        if currentnetwork==len(namesssids):
            currentnetwork=0
        result = os.popen(command.format(namesssids[currentnetwork][0],namesssids[currentnetwork][1]))
        time.sleep(4)
        wifi = subprocess.check_output(['netsh', 'WLAN', 'show', 'interfaces'])
        data = wifi.decode('iso8859-1')
        print(data)
        print(currentnetwork)
        if namesssids[currentnetwork][0] in data:
            test=True
    if test==False:
        print("Failed to connect, sorry")
        raise Exception("noWifi")
def reconnectEthernetNetwork(strAdapterName = "Remote NDIS based Internet Sharing Device"):
    import wmi
    import adminn as admin    
    if not admin.isUserAdmin():
        admin.runAsAdmin()
    import time
    c=wmi.WMI()
    qc="select * from Win32_NetworkAdapter WHERE Description ='"+strAdapterName+"'"
    o=c.query(qc)
    for conn in o:
        if conn.Description == strAdapterName or conn.name == strAdapterName:
            print(conn.name)
            if conn.NetEnabled:
                conn.Disable()
                print("reconnecting,to change 3g ip address due to dhcp")
                conn.Enable()
                time.sleep(1)
                break
            elif conn.NetEnabled==False:
                conn.Enable()

def downloadFromNetwrks(urls,method="wifi",namesssids=[]):
    global reached
    global lastAct
    global currentnetwork
    for i in range(0,len(urls)):
        url=urls[i]
        print(i)
        if i%200==0 :
            if method=="wifi":
                reconnectWiFINetwork(namesssids)
            elif method=="cle3G":
                reconnectEthernetNetwork(strAdapterName = "Remote NDIS based Internet Sharing Device")
            print(i)
        r = requests.get(url)
        reached=reached+1
        if str(r)=='<Response [200]>':
            soup = BeautifulSoup(r.content, 'html.parser')
            text=soup.find("div", {"class":"infobar"})
            if text==None:
                continue
            text=text.find_all("span", {"class":"itemprop"})
            for k in text:
                cont=k.get_text()[1:]
                if cont=='Actor' or cont=='Actress':
                    lastAct=reached
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
                        file = open(path+'\\'+str(ActorName)+'.png', "wb")
                        f = open(SaveP+'ActorsBasicDS.txt', 'a')
                        file.write(response.content)
                        if cont=="Actor":
                            f.write('\n'+ActorName+';'+'m'+';"'+photoSrc+'\"')
                        else:                            
                            f.write('\n'+ActorName+';'+'f'+';"'+photoSrc+'\"')
                        file.close()
                        f.close()  
                    else:
                        f = open(SaveP+'ActorsNoPhotoDS.txt', 'a')
                        f.write('\n'+ActorName)
                        f.close()
                        f = open(SaveP+'ActorsBasicDS.txt', 'a')
                        if cont=="Actor":
                            f.write('\n'+ActorName+';'+'m'+';'+'-')
                        else:
                            f.write('\n'+ActorName+';'+'f'+';'+'-')
                        f.close()
                    filee = open("imdbProgress.txt", "w");
                    filee.write(repr(reached));        filee.close()

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

def enrichBycle3G():
    global reached
    global lastAct
    global currentnetwork
    while reached<4300:
        try:
            downloadFromNetwrks(urls,method="wifi",namesssids=[("Galaxy A10s4751","Galaxy A10s4751")])      
        except :
            print("no wifi found")
            downloadFromNetwrks(urls,method="cle3G",namesssids=[("Galaxy A10s4751","Galaxy A10s4751")])
            filee = open("imdbProgress.txt", "w");
            filee.write(repr(reached));        filee.close()
            reconnectEthernetNetwork(strAdapterName = "Remote NDIS based Internet Sharing Device")
            print("exception accured, reconnecting")

enrichBycle3G()
