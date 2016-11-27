# loading descriptors files -> calculating score matrix for every matrices ->  finding match -> 
################################################################################################
import os
import cv2
from numpy import *
import numpy as np
from matplotlib import pyplot as plt

global count_thres
count_thres = 0.7
data = []
size = []
img_num = []
i=1

###################### loding image descriptors and storing them in data matrix ################################### 
directory = os.path.join("c:\\","/home/chandu/Desktop/project: forming collage/descriptors/")
for root,dirs,files in os.walk(directory):
	for file in files:
		if file.endswith(".txt"):
			temp = loadtxt("img"+str(i)+".txt", skiprows = 2)
			temp = temp[:,5:149]
			m,n = temp.shape
			temp = list(temp)
			data.append(temp)
			size.extend([m])
			img_num.extend([i])
			i=i+1
data = np.asarray(data)
score_mat = []
score_mat = np.asarray(score_mat)
####################### calc euclidean distance between two matrices ############################################
def distance(X,Y, score_mat):
	m = len(X)
	l = len(Y)
	score_mat = np.empty([m,l])
	for i in range(0, m):
		for j in range(0, l):
			dist = X[i] - Y[j]
			dist = dist**2
			_sum_ = sum(dist)
			euclidian_dist = np.sqrt(_sum_)
			score_mat[i,j] = euclidian_dist
	
	return score_mat

################# finding no. of similar regions between two images with the help of score matrix #################
def finding_counts(scores):
	min_thres = 150
	count = 0
	w = len(scores)
	for i in range(0,w):
		if np.any(scores[i] < min_thres): ###### count -> giving the of similar regions of data1 and data2
 			count+=1 
	return count

################### if two or more img descriptors matches then removing images from database ######################
def remove_img(count_arr,img_num, data, size):
	count_thres = 0.5
	index = [i for i, x in enumerate(count_arr) if x > count_thres]
	print "index: ", index
	for i in index:
		print "*", img_num[i]
		os.remove("/home/chandu/Desktop/project: forming collage/database/light_fruits/img"+str(img_num[i])+".pgm")
		data = np.delete(data, i, 0)
		size = np.delete(size, i, 0)
	img_num = np.delete(img_num, index, 0)
	return (img_num, data, size)
	

########################################## Main ###################################################################

w = len(size)
l = len(data)
print "len(data[1]): ", len(data[1])
while len(size)>1:	
	m = size[0]
	w = len(size)
	print img_num, size
	count_arr = []
	data1 = data[0]
	data = np.delete(data, 0, axis = 0)
	size = np.delete(size, 0, axis = 0)
	img_num = np.delete(img_num, 0, axis = 0)
	print "len(size): ", len(size)
	for j in range(0,len(size)):
		n = size[j]
		data2 = data[j]
		m = n+1
		temp_score = distance(data1, data2, score_mat)
		print "j: ", j		
		print temp_score
		count = finding_counts(temp_score)
		count = float(count)/m
		count_arr.extend([count])
	count_arr = np.asarray(count_arr)
	print count_arr
	if np.any(count_arr > count_thres):
		print "Entered"
		img_num, data, size = remove_img(count_arr,img_num, data, size)
