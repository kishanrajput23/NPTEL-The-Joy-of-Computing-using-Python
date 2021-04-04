# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 10:22:07 2021

@author: Lakhan Kumawat
"""

#Doesn't sort completely for some heavy outputs
l=input().split()
size=len(l)
swap=0
for j in range(size):
    for i in range(size-j-1):
        #print(i+j)
        if(l[i]>l[i+1]):
            swap+=1
            n1=l[i]
            l[i]=l[i+1]
            l[i+1]=n1
        

print(swap)