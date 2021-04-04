# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 12:29:23 2021

@author: Lakhan Kumawat


def rem(n):
    return n%8

def convert(li): 
      
    # Converting integer list to string list 
    s = [str(i) for i in li] 
      
    # Join list items using join() 
    res = int("".join(s)) 
      
    return(res)

def octal(n):
    if n<8:
        return n
    else:
        remlist=[]
        q=n/8
        while(q!=0):
            remlist.append(rem(n))
            n=n/8
            q=n/8
            print(remlist)
        remlist.reverse()
        st=convert(remlist)
        return st     """


def print_formatted(number):
    # your code goes here
    for i in range(1,number+1):
        print(i,binary(i))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)