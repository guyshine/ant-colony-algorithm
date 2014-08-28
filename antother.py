import numpy as np
import networkx as nx

def E(result,route):
    G=nx.Graph()
    for n in range(len(result)-1):
            #print OneAntStatus[n]
	    G.add_edge(result[n],
                        result[n+1],
                        weigh=route[result[n]][result[n+1]])
    node=G.nodes()
    su=0
    for m in range(len(node)-1):
        for n in range(m,len(node)-1):
            if (m==n):
                pass
            su=su+nx.shortest_path_length(G,m,n)
    return 1.0*su/(len(node)*(len(node)-1))

def F(result):
    G=nx.Graph()
    for n in range(len(result)-1):
        G.add_edge(result[n],result[n+1])
    result=[]
    node=G.nodes()
    for n in node:
        result.append(len(G.neighbors(n)))
    return (2.0*float(max(result)))/((len(node)*(len(node)-1))*1.0)
