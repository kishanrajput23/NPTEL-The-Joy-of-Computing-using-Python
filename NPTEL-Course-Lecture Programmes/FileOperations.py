# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 22:36:13 2021

@author: Lakhan Kumawat
"""

with open("Testing.txt","r+") as myfile:
    print(myfile.read())
    myfile.write(" I am fine is overwritten!")
myfile.close()