#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 00:18:49 2020

@author: nikunj
"""


import os
import datetime


CWD = os.getcwd()
print(CWD)

TRAIN = CWD + '/feed/train/'
TEST = CWD + '/feed/test/'

IMG_IN = CWD + '/img/img_input/'
IMG_OUT = CWD + '/data/nikunj/'

VID_IN = CWD + '/vid/vid_input/'
VID_OUT = CWD + '/vid/vid_output/'

CASCADE = CWD + '/data/'

ATT_IMG = CWD + '/att_img/'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DJANGO = os.path.join(BASE_DIR, 'face_key')
STATIC = os.path.join(DJANGO, 'static')
FILES = os.path.join(STATIC, 'files')
TRAIN_DIR = os.path.join(STATIC, 'train_images')
# FILE = FILES + '/data_' + str(datetime.datetime.now().date()) + '.txt'
