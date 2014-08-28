import numpy as np
import networkx as nx
import antGenerateGraph as agg
import antCalculateCompend as acc
import antLimith as al
import pylab as plt
import antother as ao
import copy

global Startnode 
Startnode=11
def initialization():
    global price
    global route
    global perprice
    global antcompend
    global antInf
    global nodes
    global G
    global TempAntStatus
    
    global ProblemID
    ProblemID=1

    antnum=80

    tmp = np.loadtxt("long.csv", dtype=np.str, delimiter=",")
    route = tmp[:,:].astype(np.float)
    tmp = np.loadtxt("price.csv", dtype=np.str, delimiter=",")
    perprice = tmp[:,:].astype(np.float)
    price=route*perprice
    
    antcompend=np.ones([80,80],float)*0.001
    for n in range(80):
        antcompend[n][n]=0
        
    G=nx.from_numpy_matrix(route)
    
    nodes=G.nodes()
    
    TempAntStatus=[ []for n in range(antnum)]

def initAntStatus():
    TempAntStatus=[ []for n in range(antnum)]

def MoveChoose(node):
    sum=0
    for n in range(80):
        if n!=node:
            sum=sum+antcompend[node][n]
    ProbabilityDistribution=[]
    for n in range(80):
        if n!=node:
            ProbabilityDistribution.append(1.0*antcompend[node][n]/sum)
    sumcompend=0
    random=np.random.rand()
    
    for n in range(len(ProbabilityDistribution)):
        sumcompend=sumcompend+ProbabilityDistribution[n]
        if sumcompend>=random:
            resultn=n
            break
            #print resultn

    if resultn>=node:
        resultn=resultn+1
    return resultn
def antMove(ID):
    flat = False
    while (not flat):
        antroute=[]
        antroute.append(Startnode)
        while (not (set(antroute)==set(nodes))):
            NextNode=MoveChoose(antroute[len(antroute)-1])
            antroute.append(NextNode)
        G=agg.GenerateGraph(antroute)
        flat=al.judge(G,ProblemID)
        if flat==False:
            print 'cannot complete error'
    print 'ANT '+str(ID)+' complete'
    #print len(antroute)
    TempAntStatus[ID]=antroute


if __name__ == "__main__":
    initialization()
    for item in range(10):
        print 'item '+str(item)+'start'
        for antid in range(80):
            #print 'ANT '+str(antid)+' start'
            antMove(antid)
        result=acc.CalculateCompend(TempAntStatus,antcompend,route,price)
        antcompend=copy.deepcopy(result[0])
        pprice=result[1]
        ppass=result[2]
        finalantstatus=copy.deepcopy(result[3])
        NumberOfPass=result[4]
    print antcompend
    G=agg.GenerateGraph(finalantstatus)
    print '=================result============='
    print G.edges()
    print ' '
    print pprice
    print ppass
    print 'NumberOfPass :'+str(NumberOfPass)
    print 'E :'+str(ao.E(finalantstatus,route))
    print 'F :'+str(ao.F(finalantstatus))
    nx.draw_networkx(G,pos=nx.spring_layout(G))
    plt.show()
    
        
    
