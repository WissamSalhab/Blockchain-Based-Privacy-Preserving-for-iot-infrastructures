# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 00:51:58 2021

@author: Hajerr
"""

import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt_tree.xml')
# To capture video from webcam. 
cap = cv2.VideoCapture(0); cap.release(); cap = cv2.VideoCapture("taken.mp4")
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')
# video = cv2.VideoCapture("taken.mp4")
# _, first_frame = video.read()
# first_frame=cv2.cvtColor(first_frame, cv2.COLOR_BGR2RGB)
# cv2.imshow('Window',first_frame)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# x = 300
# y = 305
# width = 100
# height = 115
# roi = first_frame[y: y + height, x: x + width]
# hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
# roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180])
# roi_hist = cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

#     _, frame = video.read()
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     mask = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
#     _, track_window = cv2.meanShift(mask, (x, y, width, height), term_criteria)
#     x, y, w, h = track_window
_, imgi = cap.read()
count=0
while cap.isOpened():
    # Read the frame

    ret, img = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        cv2.destroyWindow('img')
        break
    # if (imgi==img).all():
    #     count+=1
    #     if count==200:
    #         cv2.destroyWindow('img')
    #         print("met")
    #         break
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # if count==0:
        #     #cv2.imwrite('D:\Hajer\Face detection\Detected'+str(count)+'.jpg', img[y:y+h,x:x+h,:])
        #     count+=1
        #     cv2.imshow('shit', img[y:y+h,x:x+h,:])
        #     cv2.waitKey(10000)
        #     cv2.destroyWindow('shit')


    # Display
    cv2.imshow('img', img)
    imgi=img
    # Stop if escape key is pressed
    k = cv2.waitKey(1)
    if k==27:
        break
cv2.destroyWindow('img')
#cv2.destroyAllWindows()
# Release the VideoCapture object
cap.release()