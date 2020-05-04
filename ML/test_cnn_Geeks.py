#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:16:35 2020

@author: nikunj
"""
from PATHS import *
import cv2 
import os 
import numpy as np 
from random import shuffle 
from tqdm import tqdm 



TRAIN_DIR = TRAIN
TEST_DIR = TEST
IMG_SIZE = 50
LR = 1e-3



MODEL_NAME = 'dogsvscats-{}-{}.model'.format(LR, '6conv-basic') 

import tflearn 
from tflearn.layers.conv import conv_2d, max_pool_2d 
from tflearn.layers.core import input_data, dropout, fully_connected 
from tflearn.layers.estimator import regression 

import tensorflow as tf 
tf.reset_default_graph() 
convnet = input_data(shape =[None, IMG_SIZE, IMG_SIZE, 1], name ='input') 

convnet = conv_2d(convnet, 32, 5, activation ='relu') 
convnet = max_pool_2d(convnet, 5) 

convnet = conv_2d(convnet, 64, 5, activation ='relu') 
convnet = max_pool_2d(convnet, 5) 

convnet = conv_2d(convnet, 128, 5, activation ='relu') 
convnet = max_pool_2d(convnet, 5) 

convnet = conv_2d(convnet, 64, 5, activation ='relu') 
convnet = max_pool_2d(convnet, 5) 

convnet = conv_2d(convnet, 32, 5, activation ='relu') 
convnet = max_pool_2d(convnet, 5) 

convnet = fully_connected(convnet, 1024, activation ='relu') 
convnet = dropout(convnet, 0.8) 

convnet = fully_connected(convnet, 2, activation ='softmax') 
convnet = regression(convnet, optimizer ='adam', learning_rate = LR, 
	loss ='categorical_crossentropy', name ='targets') 


def process_test_data(): 
    testing_data = [] 
    for img in tqdm(os.listdir(TEST_DIR)): 
        path = os.path.join(TEST_DIR, img) 
        img_num = img.split('.')[0] 
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE) 
        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE)) 
        testing_data.append([np.array(img), img_num]) 
        
    shuffle(testing_data) 
    np.save('test_data.npy', testing_data) 
    return testing_data 

test_data = process_test_data()

import matplotlib.pyplot as plt 

test_data = np.load('test_data.npy', allow_pickle=True) 

fig = plt.figure() 
model = tflearn.DNN(convnet) 
model.load(CWD + '/' + MODEL_NAME, weights_only=True) 

for num, data in enumerate(test_data[:10]): 
	
	img_num = data[1] 
	img_data = data[0] 
	
	y = fig.add_subplot(4, 5, num + 1) 
	orig = img_data 
	data = img_data.reshape(IMG_SIZE, IMG_SIZE, 1) 

	# model_out = model.predict([data])[0] 
	model_out = model.predict([data])[0] 
	
	if np.argmax(model_out) == 1: str_label ='Emilia'
	else: str_label ='Kit'
		
	y.imshow(orig, cmap ='gray') 
	plt.title(str_label) 
	y.axes.get_xaxis().set_visible(False) 
	y.axes.get_yaxis().set_visible(False) 
plt.show()
