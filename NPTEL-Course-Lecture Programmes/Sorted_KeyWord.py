# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 21:03:29 2021

@author: Lakhan Kumawat
"""

#Sorted keyword in python
#lets sort a tuple
tup=("c","a","b")
print(sorted(tup))

#when we use sorted in dictionary it will by default sort by keys
dic={3:"c",2:"b",1:"a"}
print(sorted(dic))
print(dic)

#lets sort a list on the basis of length
L=["aaaa","bbb","cc"]
print(sorted(L,key=len))


#however we can use sorted to sort by other parameters

    