# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 12:16:22 2021

@author: lahza
"""

import sys
import os
import dlib
import glob
from shutil import copy
from PIL import Image
import numpy as np

BigDir="D:\\Hajer\\Face detection\\DetectedFaces - Copie (3)\\"
output_folder_path = "D:\\Hajer\\binn"
predictor_path = "D:\\Hajer\\Test DLIB\\shape_predictor_5_face_landmarks.dat"
face_rec_model_path = "D:\\Hajer\\Test DLIB\\dlib_face_recognition_resnet_model_v1.dat"

folders = list(filter(lambda x: os.path.isdir(os.path.join(BigDir, x)), os.listdir(BigDir)))
files = [file for file in os.listdir(BigDir)  if os.path.isfile(os.path.join(BigDir, file))]
faces_folder_path = BigDir
sp = dlib.shape_predictor(predictor_path)
facerec = dlib.face_recognition_model_v1(face_rec_model_path)
detector = dlib.get_frontal_face_detector()

descriptors = []
images = []
listt=[]
# for ff in files:
#     f=BigDir+ff
#     #print("Processing file {}".format(f))
#     img = dlib.load_rgb_image(f)
#     dets = detector(img, 1)
#     #print("Number of faces detected {}".format(len(dets)))
#     # Now process each face we found.
#     for k, d in enumerate(dets):
#         shape = sp(img, d)  
#         face_descriptor = facerec.compute_face_descriptor(img, shape)
#         descriptors.append(face_descriptor)
#         images.append(f)
#         #images.append((img, shape))
#     listt.append(ff)
# for i in range(len(images)):
#     listt.append(images[i][images[i].find("DetectedFrame"):])
for ff in files:
    f=BigDir+ff
    print("Processing file {}".format(f))
    img = dlib.load_rgb_image(f)
    d=dlib.rectangle(0,0,np.shape(img)[1]-1,np.shape(img)[0]-1)
    shape = sp(img,d)  
    face_descriptor = facerec.compute_face_descriptor(img,shape)
    descriptors.append(face_descriptor)
    images.append(f)
    listt.append(ff)


numberOfFiles=len(images)
i=1;h=1;
ClustersDirrr=BigDir+"cluster"+str(h).zfill(3)

SaveDirectoryCluster=[]
if not(os.path.exists(ClustersDirrr)):
    os.mkdir(ClustersDirrr)
    SaveDirectoryCluster.append(ClustersDirrr)
copy(images[0], ClustersDirrr)
i+=1


while i<numberOfFiles:
    imagesrc=BigDir+listt[i-1]
    test=False
    imageContent=Image.open(imagesrc)
    hashh = descriptors[i]
    folders = list(filter(lambda x: os.path.isdir(os.path.join(BigDir, x)), os.listdir(BigDir)))
    for kkkk in range(len(folders)):
        kk=folders[len(folders)-1-kkkk]
        listtt=os.listdir(BigDir+kk)
        for kkk in range(len(listtt)):
            otherhash=descriptors[listt.index(listtt[kkk])]
            if np.linalg.norm(np.array(otherhash)-np.array(hashh))<0.6:
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


# #print(np.linalg.norm(np.array(face_descriptor2)-np.array(face_descriptor)))
# #win = dlib.image_window();
# #img=images[34];win.clear_overlay();win.set_image(img);

labels = dlib.chinese_whispers_clustering(descriptors, 0.5)
num_classes = len(set(labels))
print("Number of clusters {}".format(num_classes))

for i in labels:
    if not(os.path.exists(BigDir+"chinesecluster"+str(i))):
        os.mkdir(BigDir+"chinesecluster"+str(i))

for i in range(len(labels)):
    copy(images[i], BigDir+"chinesecluster"+str(labels[i]))



#     # The size and padding arguments are optional with default size=150x150 and padding=0.25
#     dlib.save_face_chip(img, shape, file_path, size=150, padding=0.25)
        
    


