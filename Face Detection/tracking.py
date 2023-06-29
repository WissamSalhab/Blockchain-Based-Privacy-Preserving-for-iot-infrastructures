#!/usr/bin/python
# The contents of this file are in the public domain. See LICENSE_FOR_EXAMPLE_PROGRAMS.txt
#
# This example shows how to use the correlation_tracker from the dlib Python
# library.  This object lets you track the position of an object as it moves
# from frame to frame in a video sequence.  To use it, you give the
# correlation_tracker the bounding box of the object you want to track in the
# current video frame.  Then it will identify the location of the object in
# subsequent frames.
#
# In this particular example, we are going to run on the
# video sequence that comes with dlib, which can be found in the
# examples/video_frames folder.  This video shows a juice box sitting on a table
# and someone is waving the camera around.  The task is to track the position of
# the juice box as the camera moves around.
#
#
# COMPILING/INSTALLING THE DLIB PYTHON INTERFACE
#   You can install dlib using the command:
#       pip install dlib
#
#   Alternatively, if you want to compile dlib yourself then go into the dlib
#   root folder and run:
#       python setup.py install
#
#   Compiling dlib should work on any operating system so long as you have
#   CMake installed.  On Ubuntu, this can be done easily by running the
#   command:
#       sudo apt-get install cmake
#
#   Also note that this example requires Numpy which can be installed
#   via the command:
#       pip install numpy

import os
import glob
import cv2
import dlib
import time
# Path to the video frames
video_folder = "D:\Hajer\Face detection\\videoFrames"

# Create the correlation tracker - the object needs to be initialized
# before it can be used
tracker = dlib.correlation_tracker()
tracker2 = dlib.correlation_tracker()
face_cascade = cv2.CascadeClassifier('D:\\Hajer\\Face detection\\haarcascade_frontalface_default.xml')
win = dlib.image_window()
#win2 = dlib.image_window()
# We will track the frames as we load them off of disk

for k, f in enumerate(sorted(os.listdir(video_folder))):
    f=video_folder+"\\"+f
    time.sleep(0.1)
    print("Processing Frame {}".format(k))
    img = dlib.load_rgb_image(f)
    img2 = dlib.load_rgb_image(f)
    # We need to initialize the tracker on the first frame
    if k == 0:
        # Start a track on the juice box. If you look at the first frame you
        # will see that the juice box is contained within the bounding
        # box (74, 67, 112, 153).
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        
        
    # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            pass
        tracker.start_track(img, dlib.rectangle(x, y, x+w, y+h))
        tracker2.start_track(img2, dlib.rectangle(x, y, x+10, y+10))
    else:
        # Else we just attempt to track from the previous frame
        tracker.update(img)
        #tracker2.update(img2)
    win.clear_overlay()
    win.set_image(img)
    win.add_overlay(tracker.get_position())
    #win2.clear_overlay()
    #win2.set_image(img2)
    #win2.add_overlay(tracker2.get_position())
    dlib.hit_enter_to_continue()
    