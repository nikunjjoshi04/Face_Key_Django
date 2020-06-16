#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 00:18:49 2020

@author: nikunj
"""


import os


CWD = os.getcwd()
print(CWD)

TRAIN = CWD + '/feed/train/'
TEST = CWD + '/feed/test/'

IMG_IN = CWD + '/img/img_input/'
IMG_OUT = CWD + '/img/img_output/'

VID_IN = CWD + '/vid/vid_input/'
VID_OUT = CWD + '/vid/vid_output/'

CASCADE = CWD + '/data/'

ATT_IMG = CWD + '/att_img/'