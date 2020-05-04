#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 23:51:02 2020

@author: nikunj
"""

#Using NumPy

from PATHS import *
import cv2 as cv
import sys

img = cv.imread(IMG_IN+'1.jpg')

if img is None:
    sys.exit("Could not read the image")

cv.namedWindow('IMAGE', cv.WINDOW_NORMAL)
cv.imshow('IMAGE', img)
k = cv.waitKey(0)

if k == ord('q'):
    cv.imwrite(IMG_OUT+"nikunj.jpg", img)
    cv.destroyAllWindows()
    
elif k == ord('g'):
    cv.imwrite(IMG_OUT+"nikunj_gray.jpg", img)
    cv.destroyAllWindows()

elif k == ord('e'):
    cv.destroyAllWindows()        

