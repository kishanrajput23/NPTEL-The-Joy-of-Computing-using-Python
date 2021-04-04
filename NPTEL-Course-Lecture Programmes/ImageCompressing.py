# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 09:46:50 2021

@author: Lakhan Kumawat
"""

import numpy as np
from PIL import Image as ig

img=ig.open("lena.bmp")

pixel=img.load()

print(img.size[0])
img_new=ig.new(img.mode,img.size)

pixelNew=img_new.load()

"""
0-31=0
32-63=1
...
224-255=7
"""

#now lets convert each 255 bits to 8 bits
for i in range(img_new.size[0]):
    for j in range(img_new.size[1]):
        if (pixel[i,j]>=0 and pixel[i,j]<=31):
            pixelNew[i,j]=0
        elif (pixel[i,j]>=32 and pixel[i,j]<=63):
            pixelNew[i,j]=1
        elif pixel[i,j]>=64 and pixel[i,j]<=95:
            pixelNew[i,j]=2
        elif pixel[i,j]>=96 and pixel[i,j]<=127:
            pixelNew[i,j]=3
        elif pixel[i,j]>=128 and pixel[i,j]<=159:
            pixelNew[i,j]=4
        elif pixel[i,j]>=160 and pixel[i,j]<=191:
            pixelNew[i,j]=5
        elif pixel[i,j]>=192 and pixel[i,j]<=223:
            pixelNew[i,j]=6
        elif pixel[i,j]>=224 and pixel[i,j]<255:
            pixelNew[i,j]=7
    
    
img_new.save("Lena_compressed.bmp")
j=np.asanyarray(ig.open("lena_compressed.bmp"))