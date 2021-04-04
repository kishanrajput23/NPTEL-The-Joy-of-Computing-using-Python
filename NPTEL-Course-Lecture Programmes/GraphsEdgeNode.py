# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 21:28:52 2021

@author: Lakhan Kumawat
"""

import networkx as nx
import matplotlib.pyplot as plt
#import numpy as np
l=[1,2,3]

#lets make a graph 
G = nx.Graph()

# we can simply add edge by G.add_nodes() and can also add by this syntax given below

G.add_nodes_from(l)

#lets add edges between nodes

G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(1,3)
#print(G.edges())


#lets make another complete graph nodes in bracket()
G1=nx.complete_graph(10)

#Random Graph
G2=nx.gnp_random_graph(20,0.1) # total nodes and probability of having edge

#barabasi albert special kind of graph
G3=nx.barabasi_albert_graph(15,2) # 2 edges from each newnode to node with maximum degree


'''Uncommment these to print '''  
#nx.draw(G)
#nx.draw(G1)
#nx.draw(G2)
#nx.draw(G3)
plt.show()

#nx.write_gexf(G,"AnalysisOfGraph.gexf")

#print(G.in_edges(1))







