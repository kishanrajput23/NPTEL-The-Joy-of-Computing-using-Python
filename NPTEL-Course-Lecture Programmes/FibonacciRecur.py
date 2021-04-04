# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 11:04:49 2021

@author: Lakhan Kumawat
"""


def fibonacci(n):
    s=1
    const=n
    mylist=[0,1]
    #print(len(mylist)-1)
    while(n!=0):
        for i in range(len(mylist)-1):
            s+=mylist[i]
        if(s<const):
            mylist.append(s)
        n-=1
    print(mylist) 
    
    

n=int(input('Enter the number till which \nyou want to print fibonacci sequence : '))
fibonacci(n)
