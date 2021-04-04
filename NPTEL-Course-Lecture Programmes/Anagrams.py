# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 21:40:57 2021

@author: Lakhan Kumawat
"""

elements=int(input("Enter the number of elements : "))
mylist=[]
for _ in range(elements):
    mylist.append(input())
l=input("Enter whose anagram to be found")

for i in range(len(mylist)):
    if sorted(l)== sorted(mylist[i]):
        print("found")
        print(mylist[i])


