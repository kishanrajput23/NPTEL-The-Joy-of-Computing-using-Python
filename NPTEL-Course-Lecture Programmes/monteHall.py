# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 17:05:42 2021

@author: Lakhan Kumawat
"""

import random
doors=[0]*3
fakedoor=[0]*2
swap=0 #to store the number of swap wins
not_swap=0 #to store the non)swap wins
j=0
while(j<10):
    x=random.randint(0, 2)
    doors[x]="BMW"
    for i in range(0,3):
        if i==x:
            continue
        else:
            doors[i]="Fake"
            fakedoor.append(i)
    choice=int(input("Enter your choice in 0,1,2 : " ))
    door_open=random.choice(fakedoor)
    while(door_open==choice): #to make a different door open other than user
        door_open=random.choice(fakedoor)
    print("There is nothing in Door",door_open)
    swap_choice=input("Wanna swap ? 0/1 y/n : ")
    if(swap_choice=="y"):
        if(doors[choice]=="Fake"):
            print("Win")
            swap+=1
        else:
            print("Lose")
    else:
        if(doors[choice]=="Fake"):
            print("Lose")
        else:
            print("Win")
            not_swap+=1  
    j+=1
    
print("Swap Wins : ",swap)
print("Non Swap wins: ",not_swap)