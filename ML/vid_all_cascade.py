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

face_cascade = cv.CascadeClassifier(CASCADE + 'haarcascade_frontalface_alt2.xml')
# =============================================================================
# eye_cascade = cv.CascadeClassifier(CASCADE + 'haarcascade_eye.xml')
# profileface_cascade = cv.CascadeClassifier(CASCADE + 'haarcascade_profileface.xml')
# smile_cascade = cv.CascadeClassifier(CASCADE + 'haarcascade_smile.xml')
# fullbody_cascade = cv.CascadeClassifier(CASCADE + 'haarcascade_fullbody.xml')
# =============================================================================

upperbody_cascade = cv.CascadeClassifier(CASCADE + 'haarcascade_upperbody.xml')

cap = cv.VideoCapture(0)

i = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray)
    
# =============================================================================
#     eyes = eye_cascade.detectMultiScale(gray)
#     profilefaces = profileface_cascade.detectMultiScale(gray)
#     smiles = smile_cascade.detectMultiScale(gray)   
#     fullbodys = fullbody_cascade.detectMultiScale(gray)
# =============================================================================
    
    upperbodys = upperbody_cascade.detectMultiScale(gray)

    for (x, y, w, h) in faces: 
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
# =============================================================================
#     for (x, y, w, h) in eyes: 
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
#         
#     for (x, y, w, h) in profilefaces: 
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)    
# 
#     for (x, y, w, h) in smiles: 
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)    
#     
#     for (x, y, w, h) in fullbodys: 
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
# =============================================================================
      
    for (x, y, w, h) in upperbodys: 
         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('q'):
        break
# =============================================================================
#         re = cv.imwrite(IMG_OUT + 'Live_save' + str(i) + '.jpg', frame)
#         i += 1
#         print(re)
# =============================================================================
# =============================================================================
#     elif cv.waitKey(1) == ord('z'):
#         print(CASCADE)
#         break
# =============================================================================
        
cap.release()
cv.destroyAllWindows()
