import numpy as np
import networkx as nx
import antCalculatePass as acp

def judge(G,ProblemId):
	if ProblemId==1:
		#print 'judgeAntCalculatePass'
		#print judgeAntCalculatePass(G)
		#print 'judgeAntCalculateEdge'
		#print judgeAntCalculateEdge(G)
		#print 'judgeIegalityOfAntNodeA'
		#print judgeIegalityOfAntNodeA(G)
		return judgeAntCalculatePass(G) and judgeAntCalculatePassAnother(G) and judgeAntCalculateEdge(G) #and judgeIegalityOfAntNodeA(G)
                #
	
	if ProblemId==2:
		return False
def judgeAntCalculatePassAnother(G):
    result=acp.ReturnPossibilityOfPass(G)
    if result>=0.9:
        return True
    else:
        return False

def judgeAntCalculatePass(G):
    result=acp.ReturnNumberOfPass(G)
    if result>=0.9:
        return True
    else:
        return False

def judgeAntCalculateEdge(G):
	result=nx.number_of_edges(G)
	if result<=79:
		print 'antLimith::judgeAntCalculatePass error circle'
		return False
	else:
		return True

def judgeIegalityOfAntNodeA(G):#problem 1
	nodelist=G.nodes()
	for nodeid in nodelist:
		NodeNumberOfEdge=len(G.neighbors(nodeid))
		if NodeNumberOfEdge==1:
			return False
	return True
		
		
def judgeIegalityOfAntNodeB(G):
	print 'writing'
