# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 11:31:53 2021

@author: lahza
"""

import os
# os.remove("D:\\Hajer\\Face detection\\DetectedFaces - Copie\\DetectedFrame001Face001.jpg")
from shutil import copy

from PIL import Image
import imagehash
hashh = imagehash.average_hash(Image.open('D:\\Hajer\\Face detection\\DetectedFaces - Copie\\DetectedFrame001Face001.jpg'))

BigDir="D:\\Hajer\\Face detection\\DetectedFaces - Copie\\"
listt=os.listdir(BigDir)
numberOfFiles=len(os.listdir(BigDir))
i=1
h=1
ClustersDirrr=BigDir+"cluster"+str(h).zfill(3)

SaveDirectoryCluster=[]
if not(os.path.exists(ClustersDirrr)):
    os.mkdir(ClustersDirrr)
    SaveDirectoryCluster.append(ClustersDirrr)
copy(BigDir+listt[0], ClustersDirrr)
i+=1
while i<numberOfFiles+1:
    imagesrc=BigDir+listt[i-1]
    test=False
    imageContent=Image.open(imagesrc)
    hashh = imagehash.average_hash(imageContent)
    folders = list(filter(lambda x: os.path.isdir(os.path.join(BigDir, x)), os.listdir(BigDir)))
    for kkkk in range(len(folders)):
        kk=folders[len(folders)-1-kkkk]
        listtt=os.listdir(BigDir+kk)
        for kkk in range(len(listtt)):
            otherhash=imagehash.average_hash(Image.open(BigDir+kk+'\\'+listtt[len(listtt)-kkk-1]))
            if hashh- otherhash<7:
                copy(imagesrc, BigDir+kk)
                test=True
            if test:
                break
        if test:
            break
    if not(test):
        h+=1
        ClustersDirrr=BigDir+"cluster"+str(h).zfill(3)
        if not(os.path.exists(ClustersDirrr)):
            os.mkdir(ClustersDirrr)
            SaveDirectoryCluster.append(ClustersDirrr)
        copy(imagesrc, ClustersDirrr)
    i+=1

# listt=os.listdir(BigDir)
# ClustersDirrr=BigDir+"falsefaces"

# SaveDirectoryCluster=[]
# if not(os.path.exists(ClustersDirrr)):
#     os.mkdir(ClustersDirrr)
# for kkkk in folders:
#     o=BigDir+kkkk
#     listtt=os.listdir(o)
#     image = face_recognition.load_image_file(o+'\\'+listtt[0] )
#     face_locations = face_recognition.face_locations(image)
#     if len(face_locations)==0:
#         copy(o+'\\'+listtt[0], ClustersDirrr)
        
# import face_recognition

# for kkkk in range(len(folders)):
#     kk=folders[kkkk]
#     listtt=os.listdir(BigDir+kk)
#     for k in listtt:
#         hashh = imagehash.average_hash(Image.open('D:\\Hajer\\Face detection\\DetectedFaces - Copie\\DetectedFrame001Face001.jpg'))

# folders = list(filter(lambda x: os.path.isdir(os.path.join(BigDir, x)), os.listdir(BigDir)))

# for kkkk in range(1,len(folders)):
#     kk=folders[kkkk]
#     listtt=os.listdir(BigDir+kk)
#     for k in listtt
#     hashh = imagehash.average_hash(Image.open('D:\\Hajer\\Face detection\\DetectedFaces - Copie\\DetectedFrame001Face001.jpg'))
    
    



