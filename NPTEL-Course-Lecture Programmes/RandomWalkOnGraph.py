# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 12:51:16 2021

@author: Lakhan Kumawat
"""

import networkx as nx
import random
import matplotlib.pyplot as plt
import operator


G=nx.gnp_random_graph(10,0.5,directed=True)

nx.draw(G,with_labels=True)
plt.show()

#x is a random source node
x=random.choice([i for i in range(G.number_of_nodes())])

dic_counter={} #to count the no of visit to nodes

for  i in range(G.number_of_nodes()):
    dic_counter[i]=0
    
dic_counter[x]+=1

for i in range(10000):
    list_n=list(G.neighbors(x)) #Get all the nodes of current node
    
    if(len(list_n)==0): #x is a leaf node no further traversal so choose a node randomly from graph to continue visit
        x=random.choice([ i for i in range(G.number_of_nodes(x))])
        dic_counter[x]+=1
    else:
        x=random.choice(list_n)
        dic_counter[x]+=1
        
#lets check the ranodmness by using python inbuilt function
p=nx.pagerank(G)

sorted_p=sorted(p.items(),key=operator.itemgetter(1)) #sorts on the basis of keys

sorted_d=sorted(dic_counter.items(),key=operator.itemgetter(1))


print("I Applied : ",sorted_d)
print("Machine applied : ",sorted_p)
    