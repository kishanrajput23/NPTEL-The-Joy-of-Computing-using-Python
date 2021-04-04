# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 21:37:05 2021

@author: Lakhan Kumawat
"""

import numpy as np
from PIL import Image

#basically image is a matrix 
#dtype is datatype to be stored in matrix it is unsigned int 8 bits
array1=np.zeros([100,200,3],dtype=np.uint8)
array1[:,:100]=[200,128,61] #orange color
array1[:,100:]=[60,128,80]
#to make a image from the 2d matrix we made and provide rgb formats
img=Image.fromarray(array1)

#save the image
img.save("RGB-Format.png")
print("DONE!!!")
