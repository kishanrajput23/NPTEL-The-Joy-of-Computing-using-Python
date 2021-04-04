# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 13:45:46 2021

@author: Lakhan Kumawat
"""

mylist=input().split()
k=int(input())
k1=k
mylist1=mylist
mylist1.sort()
mylist.sort()
max1=max(mylist1)
#print(mylist,mylist1)
#remove k-1th max from list1 and print max
while(k1-1!=0):
    while(max(mylist1)==max1):
        mylist1.remove(max(mylist1))
        
    max1=max(mylist1)
    k1-=1
    
#remove k-1th min from list and print min
min2=min(mylist)
while(k-1!=0):
    while(min(mylist)==min2):
        mylist.remove(min(mylist))
        
    min2=min(mylist1)
    k-=1

#finally sum of kth max and kth min
print(int(max(mylist1))+int(min(mylist)))