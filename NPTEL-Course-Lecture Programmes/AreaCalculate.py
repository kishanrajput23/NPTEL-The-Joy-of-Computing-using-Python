# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:37:40 2021

@author: Lakhan Kumawat
"""

#here we will write a program to count the area of rajasthan

#import image library from PIL

#india rgba(254,190,109,255)
#◘uja☻at rgba(238,28,37,255) ☺☻♥♦♣♠•◘○


from PIL import Image as im
#import numpy as np
import random 

img=im.open("India.jpg")
rbg_img=img.convert("RGB")
count_guj=0
count_in=0
count=0
while(count<=10000):
    x=random.randint(0,789) #select a random point in image x and y are inverted in python
    y=random.randint(0,899)
    z=0
    r,g,b=rbg_img.getpixel((x,y))
    if(r==254):
        count_in+=1
        count+=1
    elif r==238:
        count_guj+=1
        count+=1
    else:
        count+=1
        
        
area_guj=(count_guj/count_in)*3287263
print(area_guj)