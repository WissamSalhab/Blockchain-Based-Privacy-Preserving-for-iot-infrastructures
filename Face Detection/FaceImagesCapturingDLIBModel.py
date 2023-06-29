import cv2
import os
import sys
import dlib
import glob
from shutil import copy
import numpy as np

# Load the cascade
def ShowAndSaveDetectedFaces(SaveDirectory="D:\Hajer\Face detection\\",video="D:\\Hajer\\Face detection\\taken.mp4",predictor_path = "D:\\Hajer\\Test DLIB\\shape_predictor_5_face_landmarks.dat"):
    if not(os.path.exists(SaveDirectory+"DetectedFaces")):
        path = os.path.join(SaveDirectory, "DetectedFaces")
        os.mkdir(path)
        SaveDirectory=path
    else:
        path = os.path.join(SaveDirectory, "DetectedFaces")
        SaveDirectory=path    
    cap = cv2.VideoCapture(video)
    sp = dlib.shape_predictor(predictor_path)
    detector = dlib.get_frontal_face_detector()

    CurrentFrame=0
    while cap.isOpened():
        ret, img = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            cv2.destroyWindow('img')
            break
        CurrentFrame+=1
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        dets = detector(img, 1)
        faces = []
        for i,d in enumerate(dets):
            faces.append([d.left(),d.top(),d.right()-d.left(),d.bottom()-d.top()])
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
    
def ShowAndSaveDetectedFacesBackend(SaveDirectory="D:\Hajer\Face detection\\",video="D:\\Hajer\\Face detection\\taken.mp4",predictor_path = "D:\\Hajer\\Test DLIB\\shape_predictor_5_face_landmarks.dat"):
    if not(os.path.exists(SaveDirectory+"DetectedFaces")):
        path = os.path.join(SaveDirectory, "DetectedFaces")
        os.mkdir(path)
        SaveDirectory=path
    else:
        path = os.path.join(SaveDirectory, "DetectedFaces")
        SaveDirectory=path    
    cap = cv2.VideoCapture(video)
    sp = dlib.shape_predictor(predictor_path)
    detector = dlib.get_frontal_face_detector()
    CurrentFrame=0
    while cap.isOpened():
        ret, img = cap.read()
        print(CurrentFrame)
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        CurrentFrame+=1
        dets = detector(img, 1);    faces = []
        for i,d in enumerate(dets):
            topp=d.top()
            leftt=d.left()
            rightt=d.right()
            bottomm=d.bottom()
            if leftt<0 or topp<0 or rightt>np.shape(img)[1] or bottomm>np.shape(img)[0]:
                if leftt<0:
                    leftt=0
                elif topp<0:
                    topp=0
                elif rightt>np.shape(img)[1]:
                    rightt=np.shape(img)[1]
                elif bottomm>np.shape(img)[0]:
                    bottomm=np.shape(img)[0]
            faces.append([leftt,topp,rightt-leftt,bottomm-topp])
        FaceInFrameCount=0
        for (x, y, w, h) in faces:
            FaceInFrameCount+=1
            cv2.imwrite(SaveDirectory+'\DetectedFrame'+str(CurrentFrame).zfill(3)+'Face'+str(FaceInFrameCount).zfill(3)+'.jpg', img[y:y+h,x:x+h,:])            
    cap.release()
    
    
ShowAndSaveDetectedFacesBackend(SaveDirectory="D:\Hajer\Face detection\\")
