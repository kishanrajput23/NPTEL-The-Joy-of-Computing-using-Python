# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 21:41:10 2021

@author: Lakhan Kumawat

A Tuple is a collection of Python objects separated by commas. 
In someways a tuple is similar to a list in terms of indexing,
 nested objects and repetition but a tuple is immutable unlike lists which are mutable.
 
 Tuples are faster to access than lists since they are immutable

just like in list we have []
and in dictionary {}
in tuple we have
"""
tuple1 = (0, 1, 2, 3) 

  
tuple2=("Buggati","RolceRoyce","Strawberry","Buggati")
print(tuple2)


# Concatenating above two 
print(tuple1 + tuple2) 

#print length
print(len(tuple2)) 

#prints the no. of times buggati arrived in tuple :D
print(tuple2.count("Buggati"))

#prints the index of the no or word (considers first occurence)
print("Index of strawberry tuple data is : ",tuple2.index("Strawberry"))

#tuple repetition
tuple3 = ('python',)*3
print(tuple3) 