import numpy as np
import networkx as nx
import pylab as plt
def GenerateGraph(route):
    longn=len(route)
    G=nx.Graph()
    for node in range(longn-1):
        G.add_edge(route[node],route[node+1])
    return G

if __name__ == "__main__":
    testn=[1,2,1,3,4,2,3,1,4,2,3,1]
    GG=GenerateGraph(testn)
    print GG.nodes()
    GG.add_edge(1,2,weigh=1)
    GG.add_edge(3,2,weigh=2)
    GG.add_edge(3,4,weigh=3)
    GG.add_edge(1,4,weigh=4)
    GG.add_edge(1,3,weigh=5)
    GG.add_edge(2,4,weigh=6)
    print GG.edges()
    print GG.neighbors(1)
    pos=nx.spring_layout(GG)
    color=nx.get_edge_attributes(GG,'weigh')
    nx.draw_networkx_edges(GG, pos,edgelist=color.keys(),edges_color=color.values())
    #nx.draw(GG)
    plt.show()
    
