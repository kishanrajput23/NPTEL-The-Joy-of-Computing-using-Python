# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 21:06:31 2021

@author: Lakhan Kumawat
"""

import random
import matplotlib.pyplot as plt
account=0
x=[]
y=[]
for i in range(365):
    x.append(i+1)
    bet=random.randint(1,10)
    luck=random.randint(1,10)
    
    if bet==luck:
        account+=900-100 #100 participation fee
    else:
        account-=100
    y.append(account)
    
print("Amount in your game account: ",account)
plt.plot(x,y)
plt.xlabel("money")
plt.ylabel("days")
plt.show()
