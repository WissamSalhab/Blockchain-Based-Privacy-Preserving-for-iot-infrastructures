# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 07:37:21 2021

@author: Hajer
"""
import cv2
import os
# Load the cascade
def ShowAndSaveDetectedFaces(SaveDirectory="D:\Hajer\Face detection\\",video="D:\\Hajer\\Face detection\\taken.mp4"):
    if not(os.path.exists(SaveDirectory+"DetectedFaces")):
        path = os.path.join(SaveDirectory, "DetectedFaces")
        os.mkdir(path)
        SaveDirectory=path
    else:
        path = os.path.join(SaveDirectory, "DetectedFaces")
        SaveDirectory=path    
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(video)

    CurrentFrame=0
    while cap.isOpened():
        ret, img = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            cv2.destroyWindow('img')
            break
        CurrentFrame+=1
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        FaceInFrameCount=0
        for (x, y, w, h) in faces:
            FaceInFrameCount+=1
            #cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.imwrite(SaveDirectory+'\DetectedFrame'+str(CurrentFrame).zfill(3)+'Face'+str(FaceInFrameCount).zfill(3)+'.jpg', img[y:y+h,x:x+h,:])
            
        
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # Display
        cv2.imshow('img', img)
        # Stop if escape key is pressed
        k = cv2.waitKey(1)
        if k==27:
            break
    cv2.destroyWindow('img')
    cap.release()
    
def ShowAndSaveDetectedFacesBackend(SaveDirectory="D:\Hajer\Face detection\\",video="D:\\Hajer\\Face detection\\taken.mp4"):
    if not(os.path.exists(SaveDirectory+"DetectedFaces")):
        path = os.path.join(SaveDirectory, "DetectedFaces")
        os.mkdir(path)
        SaveDirectory=path
    else:
        path = os.path.join(SaveDirectory, "DetectedFaces")
        SaveDirectory=path
        
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(video)
    countDetectedFaces=0
    while cap.isOpened():
        ret, img = cap.read()
        countDetectedFaces+=1
        if not ret:
            break
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            #cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.imwrite(SaveDirectory+'\Detected'+str(countDetectedFaces).zfill(3)+'.jpg', img[y:y+h,x:x+h,:])
            countDetectedFaces+=1
    cap.release()


ShowAndSaveDetectedFaces(SaveDirectory="D:\Hajer\Face detection\\")

