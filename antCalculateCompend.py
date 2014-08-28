import numpy as np
import networkx as nx
import antCalculatePass as acp
import antGenerateGraph as agg
import copy
import pylab as plt
import antother as ao
def Deal(OneAntStatus,route,Price):
	#print len (OneAntStatus)
	G=nx.Graph()
	for n in range(len(OneAntStatus)-1):
                #print OneAntStatus[n]
		G.add_edge(OneAntStatus[n],
                           OneAntStatus[n+1],
                           weigh=route[OneAntStatus[n]][OneAntStatus[n+1]],
                           price=Price[OneAntStatus[n]][OneAntStatus[n+1]])
		
	#print 'this is  of data'
	#print ' | - |'+ str(len (OneAntStatus))
	#print ' | - |'+ str(G.number_of_edges())
	return G

##def UnitaryList(data):
##	mmax=max(data)
##	mmin=min(data)
##	for n in range(len(data)):
##		#print data[n][0]
##		#print type(mmin)
##		print mmin[0]
##		print mmax[0]
##		#print type(mmax)
##		#print type(data[n][0])
##		data[n][0]=(float(data[n][0])*1.0-float(mmin[0])*1.0)/(float(mmax[0])*1.0-float(mmin[0])*1.0)
##	return data

def UnitaryList(data):
	for n in range(len(data)):
		data[n]=np.log10(data[n])
	return data
		
def CalculateCompend(AntStatus,Antcompend,route,Price):
        
	AntN=np.size(AntStatus)
	resultcompend=[]
	resultprice=[]
	resultPossibilityOfPass=[]
	resultweigh=[]
	resultNumberOfPass=[]
	for n in range(AntN):
		G=copy.deepcopy(Deal(AntStatus[n],route,Price))
		price=G.size(weight='price')
		print 'doing'
		weigh=G.size(weight='weigh')
		PossibilityOfPass=acp.ReturnPossibilityOfPass(agg.GenerateGraph(AntStatus[n]))
		NumberOfPass=acp.ReturnNumberOfPass(agg.GenerateGraph(AntStatus[n]))
		resultprice.append(price)
		resultPossibilityOfPass.append(PossibilityOfPass)
		resultNumberOfPass.append(NumberOfPass)
		resultweigh.append(weigh)


	rresultPossibilityOfPass=UnitaryList(copy.deepcopy(resultPossibilityOfPass))
	rresultweigh=UnitaryList(copy.deepcopy(resultweigh))
	rresultprice=UnitaryList(copy.deepcopy(resultprice))
	
	for n in range(AntN):
		 resultcompend.append(4200000/rresultprice[n]+1.4/ao.E(AntStatus[n],route)+0.004/ao.F(AntStatus[n]))
	#rresultPossibilityOfPass[n]/0.9+
	MAXresultcompend=max(resultcompend)
	INDEXresultcompend=resultcompend.index(MAXresultcompend)
	G=agg.GenerateGraph(AntStatus[INDEXresultcompend])
	print "price:   "+str(resultprice[INDEXresultcompend])
	print "Pass :   "+str(resultPossibilityOfPass[INDEXresultcompend])
	edges=G.edges()
	Antcompend=Antcompend*0.8
	for e in edges:
		 Antcompend[e[0]][e[1]]=Antcompend[e[0]][e[1]]+MAXresultcompend
		 Antcompend[e[1]][e[0]]=Antcompend[e[1]][e[0]]+MAXresultcompend
	return [Antcompend,
                resultprice[INDEXresultcompend],
                resultPossibilityOfPass[INDEXresultcompend],
                AntStatus[INDEXresultcompend],
                resultNumberOfPass[INDEXresultcompend]]
