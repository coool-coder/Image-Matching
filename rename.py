import os
import cv2
from numpy import *
import numpy as np


i=1
directory = os.path.join("c:\\","/home/chandu/Desktop/project: forming collage/paris_attacks/test_data")
dir2 = os.path.join("c:\\","/home/chandu/Desktop/project: forming collage/paris_attacks/test1")
for root,dirs,files in os.walk(directory):
	for file in files:
  		image = cv2.imread(os.path.join(directory, file))
		# cv2.imshow("file", image)
		target = os.path.join(dir2, "img"+str(i)+".png")
		cv2.imwrite(target,image)
		os.remove(os.path.join(directory, file))
		i=i+1

		cv2.waitKey(550)