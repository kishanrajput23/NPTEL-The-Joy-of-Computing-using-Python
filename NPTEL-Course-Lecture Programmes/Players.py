# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 22:44:01 2021

@author: Lakhan Kumawat
"""

import random

def choose():
    words=['ram','lakhan','abhishek']
    pick=random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def display(p1name,p2name,pp1,pp2):
    print(p1name," : ",pp1)
    print(p2name," : ",pp2)
    

def play():
    p1name = input("Player 1, please enter your name")
    p2name = input("Player 2, please enter your name")
    pp1=0
    pp2=0
    turn=0
    while(1):
        #computer's task
            picked_word=choose()
            qn=jumble(picked_word)
            print("Solve this : ",qn)
            #player 1
            if turn%2==0:
                print(p1name," its your turn")
                turn+=1
                ans = input("Please enter : ")
                if ans==picked_word:
                    pp1+=1
                    print("You were right :)")
                else:
                    print("better luck next time")
                    
            else:
                print(p2name," its your turn")
                turn+=1
                ans = input("Please enter : ")
                if ans==picked_word:
                    pp2+=1
                else:
                    print("better luck next time")
                choice=int(input("Continue 0 / exit 1"))
                if choice==0:
                    print("Another one ")
                else:
                    display(p1name,p2name,pp1,pp2)
                    break
                
play()
            
