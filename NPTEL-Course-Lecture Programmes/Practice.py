
import networkx as nx
import random as R
import matplotlib.pyplot as plt

def add_edges():
    nodes=list(G.nodes())
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if nodes[j]!=nodes[i]:
                rand=R.random()
                if rand<0.5:
                    G.add_edge(i,j)

    return G

def assign_points(G):
    nodes=list(G.nodes())
    p=[]
    for _ in nodes:
        p.append(100)
    return p


def distribute_points(G,points):
    nodes=list(G.nodes())
    new_points=[]
    for i in range(len(nodes)):
        new_points.append(0)
        
    for n in nodes:
        out=list(G.out_edges(n))
        if len(out):
            share=points[n]/len(out)
            for (src,tgt) in out:
                new_points[tgt]+=share
        else:
            new_points[n]=new_points[n]+points[n]
    return new_points


def keep_distributing(points,G):
    
    while(1):
        new_pt=distribute_points(G,points)
        print(new_pt)
        points=new_pt
        stop=input("Press # to stop ,enter to continue")
        if stop=="#":
            break
    return new_pt


def rank_points(final_points):
    #make a dictionary to assign key value pair
    d={}
    for i in range(len(final_points)):
        #Assigning key with points
        d[i]=final_points[i]
     
        #sort the dictionary on the basis of key which is here function lambda
        # where f is representing the dictionary f[1] denotes value at index 1
    print(sorted(d.items(),key=lambda f:f[1]))
        

G=nx.DiGraph()
G.add_nodes_from([i for i in range(10)])
G=add_edges()

#Add labels to nodes
nx.draw(G,with_labels=True)


#Assign points to each nodes so that we can distribute later
points = assign_points(G)


#distribute points
final_points=keep_distributing(points,G)


#rank all the points
rank_points(final_points)


#lets compare with default networkx function to check whether our calculated results are matching the values calculated by default functions itself
result=nx.pagerank(G) #Gives more upto 2 decimal places compared to our results
print(sorted(result.items(),key=lambda f:f[1]))

nx.draw(G)
plt.show()




