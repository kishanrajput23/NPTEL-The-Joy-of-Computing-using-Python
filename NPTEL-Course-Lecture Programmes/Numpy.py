# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 09:23:18 2021

@author: Lakhan Kumawat
"""
import numpy as np

a=np.array([1,2,3])

#Type array
print(type(a))

#shape (row,col)
print(a.shape)

print(a[0],a[1])

a[1]=6

print(a[1])


b = np.zeros((2,2))

print(b)

c = np.ones((2,2))

print(c)

d=np.full((2,2),5)

print(d)

e=np.random.random((2,2))

print(e)

#typecasting a array
f=np.array([1,2],dtype=np.int64)

print(f.dtype)

# we can also type cast to float 64 //or data to identify itself

g=np.array([0.0,2.0])

print(g.dtype)


h=np.array([[1,2],[3,4]])

#transpose
print(h.T)

#sum of x ele
print(np.sum(h))


#sum of col1 and col2

print(np.sum(h,axis=0))

print(np.sum(h,axis=1))

print(np.multiply(h,g))

print(h-g) # or h+g or np.subtract(h,g) np.addition(h,g)

print(np.sqrt(h))