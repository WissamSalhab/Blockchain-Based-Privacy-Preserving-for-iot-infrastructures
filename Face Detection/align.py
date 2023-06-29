# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 07:31:55 2021

@author: lahza
"""
import sys
import dlib
import time

predictor_path = "D:\\Hajer\\Test DLIB\\shape_predictor_5_face_landmarks.dat"

detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor(predictor_path)
face_file_path="D:\\Hajer\\Face detection\\test3.jpg"
face_directory_path="D:\\Hajer\\Scrapper\\"
face_directory_pathM=face_directory_path+"Actors\\"
face_directory_pathF=face_directory_path+"Actresses\\"


img = dlib.load_rgb_image(face_file_path)
dets = detector(img, 1)
num_faces = len(dets)
if num_faces == 0:
    print("Sorry, there were no faces found in '{}'".format(face_file_path))
    exit()
faces = dlib.full_object_detections()
for detection in dets:
    faces.append(sp(img, detection))

window = dlib.image_window()

# Get the aligned face images
# Optionally: 
images = dlib.get_face_chips(img, faces, size=360, padding=0.25)
#images = dlib.get_face_chips(img, faces, size=320)
for image in images:
    time.sleep(2)
    window.set_image(image)
    dlib.hit_enter_to_continue()

