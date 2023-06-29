# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 16:41:37 2021

@author: lahza
"""

import cv2
import os

def SaveVideoFrames(SaveDirectory="D:\Hajer\Face detection\\",video="D:\\Hajer\\Face detection\\taken.mp4"):
    if not(os.path.exists(SaveDirectory+"videoFrames")):
        path = os.path.join(SaveDirectory, "videoFrames")
        os.mkdir(path)
        SaveDirectory=path
    else:
        path = os.path.join(SaveDirectory, "videoFrames")
        SaveDirectory=path    
    cap = cv2.VideoCapture(video)
    CurrentFrame=0
    while cap.isOpened():
        ret, img = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            cv2.destroyWindow('img')
            break
        CurrentFrame+=1
        cv2.imwrite(SaveDirectory+'\DetectedFrame'+str(CurrentFrame).zfill(3)+'.png', img)
    cap.release()
SaveVideoFrames(SaveDirectory="D:\Hajer\Face detection\\",video="D:\\Hajer\\Face detection\\taken.mp4")



