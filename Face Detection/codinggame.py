# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 22:39:35 2021

@author: lahza
"""
# import cv2
# import face_recognition
# image = face_recognition.load_image_file("D:\\Hajer\\Face detection\\DetectedFaces\\DetectedFrame066Face001.jpg" )
# face_locations = face_recognition.face_locations(image)

# cv2.imshow('shit', image[face_locations[0][0]:face_locations[0][1],face_locations[0][3]:face_locations[0][2],:])
# cv2.waitKey(10000)
# cv2.destroyWindow('shit')

import sys
import os
import dlib
from shutil import copy

detector = dlib.get_frontal_face_detector()
win = dlib.image_window()

BigDir="D:\\Hajer\\Face detection\\DetectedFaces - Copie\\"
folders = list(filter(lambda x: os.path.isdir(os.path.join(BigDir, x)), os.listdir(BigDir)))
files = [file for file in os.listdir(BigDir)  if os.path.isfile(os.path.join(BigDir, file))]

ClustersDirrr=BigDir+"falsefaces"


kk=0
for f in files:
    f=BigDir+f
    print("Processing file: {}".format(f))
    img = dlib.load_rgb_image(f)
    # The 1 in the second argument indicates that we should upsample the image
    # 1 time.  
    dets = detector(img, 1)
    print("Number of faces detected: {}".format(len(dets)))
    kk+=len(dets)
    if len(dets)==0:
        copy(f, ClustersDirrr)
    for i, d in enumerate(dets):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
            i, d.left(), d.top(), d.right(), d.bottom()))

    win.clear_overlay()
    win.set_image(img)
    win.add_overlay(dets)
    dlib.hit_enter_to_continue()

import sys
import os
import dlib
import glob

BigDir="D:\\Hajer\\Face detection\\DetectedFaces - Copie\\"
predictor_path = "D:\\Hajer\\Test DLIB\\shape_predictor_5_face_landmarks.dat"
face_rec_model_path = "D:\\Hajer\\Test DLIB\\dlib_face_recognition_resnet_model_v1.dat"
faces_folder_path = BigDir
# Load all the models we need: a detector to find the faces, a shape predictor
# to find face landmarks so we can precisely localize the face, and finally the
# face recognition model.
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor(predictor_path)
facerec = dlib.face_recognition_model_v1(face_rec_model_path)
win = dlib.image_window()

f=BigDir+files[2]
img = dlib.load_rgb_image(f)
dets = detector(img, 1)
print("Number of faces detected: {}".format(len(dets)))

# Now process each face we found.
for k, d in enumerate(dets):
    print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
        k, d.left(), d.top(), d.right(), d.bottom()))
    # Get the landmarks/parts for the face in box d.
    shape = sp(img, d)
    face_descriptor = facerec.compute_face_descriptor(img, shape)
    # Draw the face landmarks on the screen so we can see what face is currently being processed.

import numpy as np
#print(np.linalg.norm(np.array(face_descriptor2)-np.array(face_descriptor)))
#img=images[34];win.clear_overlay();win.set_image(img);
win.clear_overlay()
win.set_image(img)
shape = sp(img, img)


win.clear_overlay()
win.add_overlay(d)
win.add_overlay(shape)





