#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 14:18:13 2020

@author: nikunj
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 23:28:07 2020

@author: nikunj
"""
from PATHS import *
import os
import numpy as np
import cv2 as cv
import math as m
import pickle

color = (160,160,160)
thik = 2
i = 0
font = cv.FONT_HERSHEY_SIMPLEX
col = (0, 255, 0)

def my_angle(img,c,r,w,h,color,thik):
#     print(img,c,r,w,h,color,thik)
    
    cv.line(img, (c,r), (c+m.floor((w/4)+(w/2)/4),r), color, thik)
    cv.line(img, (c+m.floor((w/2)+(w/2)/4),r), (c+w,r), color, thik)
    
    cv.line(img, (c,r), (c,r+m.floor((h/4)+(h/2)/4)), color, thik)
    cv.line(img, (c,r+m.floor((h/2)+(h/2)/4)), (c,r+h), color, thik)
    
    cv.line(img, (c,r+h), (c+m.floor((w/4)+(w/2)/4),r+h), color, thik)
    cv.line(img, (c+m.floor((w/2)+(w/2)/4),r+h), (c+w,r+h), color, thik)
    
    cv.line(img, (c+w,r), (c+w,r+m.floor((h/4)+(h/2)/4)), color, thik)
    cv.line(img, (c+w,r+m.floor((w/2)+(w/2)/4)), (c+w,r+h), color, thik)


face_cascade = cv.CascadeClassifier(CASCADE + 'haarcascade_frontalface_alt2.xml')
#profileface_cascade = cv.CascadeClassifier(CASCADE + 'haarcascade_profileface.xml')


cap = cv.VideoCapture(0)
i = 0
roi = np.zeros((2,3))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray)
 #   profilefaces = profileface_cascade.detectMultiScale(gray)


    for (x, y, w, h) in faces:
        roi = frame[y:y+h, x:x+w] 
        
        my_angle(frame,x,y,w,h,color,thik)
        
        
# =============================================================================
#     for (x, y, w, h) in profilefaces: 
#         my_angle(frame,x,y,w,h,color,thik)
# =============================================================================

    
    cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('q'):
        re = cv.imwrite(IMG_OUT + 'Live_save' + str(i) + '.jpg', roi)
        break
        
cap.release()
cv.destroyAllWindows()
