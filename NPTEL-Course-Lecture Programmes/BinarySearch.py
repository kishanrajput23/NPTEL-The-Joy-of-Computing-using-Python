# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 16:46:30 2021

@author: Lakhan Kumawat
"""

#binary search
def binary_search(start,end,l,x):
    if start==end:
        if l[end]==x:
            return end
        else:
            return -1
    else:
        mid=int((start+end)/2)
        if(l[mid]==x):
            return mid
        elif(l[mid]>x):
            return binary_search(start,mid-1, l,x)
        elif(l[mid]<x):
            return binary_search(mid +1 ,end,l,x)
    
    
    
    
    
b=int(input("Input any number you want to perform binary search : "))
mylist=[1,2,3,4,5,6,7,8,9,10]
#print(mylist[0])
print(1+binary_search(0,len(mylist)-1,mylist,b))