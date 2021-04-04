# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 21:17:02 2021

@author: Lakhan Kumawat
"""
#Flipping the image
from PIL import Image

#opening the image
img = Image.open('Recipt.jpg')

#transpose of the matrix
transposed_img=img.transpose(Image.FLIP_LEFT_RIGHT)

#save it in a new file

transposed_img.save("Corrected.png")

print("Done!")
