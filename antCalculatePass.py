import numpy  as np
import networkx as nx
import antGenerateGraph as agg
import pylab as plt
import copy
def ReturnNumberOfPass(G):
    NumberNode=nx.number_of_nodes(G)
    nodes=G.edges(G)
    large=[]
    for edges in nodes:
        TempG=copy.deepcopy (G)
        TempG.remove_edge(edges[0],edges[1])    
        if (nx.is_connected(TempG)):
            pass
        else:
            NumberPart=nx.number_connected_components(TempG)
            Part=nx.connected_components(TempG)
            connected_components=sorted(nx.connected_components(TempG),key=len,reverse=True)
            TempLarge=[]
            for n in range(NumberPart):        
                TempLarge.append(len(connected_components[n]))
            large.append(min(TempLarge))
    if large==[]:
        return 100.0
    else:
        return 1.0*(NumberNode-max(large))/NumberNode


def ReturnPossibilityOfPass(G):
    nodes=G.nodes()
    NumberNode=nx.number_of_nodes(G)
    sum=0
    for n in range(NumberNode):
        TempG=copy.deepcopy (G)
        TempG.remove_node(nodes[n])
        if (nx.is_connected(TempG)):
            sum=sum+1
    return 1.0*sum/NumberNode
            
          
if __name__ == "__main__":
    testn=[1,2,3,2,4,2,5,3,5,4]
    GG=agg.GenerateGraph(testn)
    print ReturnPossibilityOfPass(GG)
    nx.draw(GG)
    plt.show()
