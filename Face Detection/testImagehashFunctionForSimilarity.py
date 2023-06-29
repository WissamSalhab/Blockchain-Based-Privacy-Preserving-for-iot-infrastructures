# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 22:41:43 2021

@author: lahza
"""

import os
# os.remove("D:\\Hajer\\Face detection\\DetectedFaces - Copie\\DetectedFrame001Face001.jpg")

from PIL import Image
import imagehash
hashh = imagehash.average_hash(Image.open('D:\\Hajer\\Face detection\\DetectedFaces - Copie\\DetectedFrame001Face001.jpg'))
print(hashh)

otherhash = imagehash.average_hash(Image.open('D:\\Hajer\\Face detection\\DetectedFaces - Copie\\DetectedFrame025Face001.jpg'))
print(otherhash)

print(hashh == otherhash)
print(hashh - otherhash)
print(hashh - otherhash < 15)








