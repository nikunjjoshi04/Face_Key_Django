#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 02:31:33 2020

@author: nikunj
"""

from PATHS import *
import os
import cv2 as cv
import cv2
from PIL import Image
import numpy as np
import pickle


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, 'feed')

face_cascade = cv.CascadeClassifier(CASCADE + 'haarcascade_frontalface_alt2.xml')
recognizer = cv.face.LBPHFaceRecognizer_create()

x_train = []
y_lables = []

current_id = 0
lable_ids = {}

for root, dirs, files in os.walk(IMAGE_DIR):
    for file in files:
        if file.endswith('png') or file.endswith('jpg') or file.endswith('jpeg'):
            path = os.path.join(root, file)
            lable = os.path.basename(root).replace(' ', '-').lower()
            print(lable)
            
            if not lable in lable_ids:
                lable_ids[lable] = current_id
                current_id += 1
            id_ = lable_ids[lable]
            
            pil_image = Image.open(path).convert('L')
            image_array = np.array(pil_image, 'uint8')
            #print(image_array)
            faces = face_cascade.detectMultiScale(image_array)
            
            for (x, y, w, h) in faces: 
                roi = image_array[y:y+h, x:x+w] 
                x_train.append(roi)
                y_lables.append(id_)


with open('labels.pickle', 'wb') as f:
    pickle.dump(lable_ids, f)


recognizer.train(x_train, np.array(y_lables))
recognizer.save("trainner.yml")

# =============================================================================
# print(y_lables)
# print(x_train)            
# print(lable_ids)
# =============================================================================




















