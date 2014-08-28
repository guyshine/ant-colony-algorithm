import numpy as np
import networkx as nx
import pylab as plt
def report(antcompend):
	G=nx.graph()
	G=from_numpy_matrix(antcompend)
	noden=nx.number_of_nodes(G)
	for n in range(noden):
		for nn in range(noden):
			if n==nn:
				pass
			G.add_edge(n,nn,weigh=route[n][nn])
	pos=nx.spring_layout(T)
	
	plt.figure(figsize=(8,8))
	nx.draw_networkx_nodes(G,pos)
	nx.draw_networkx_edges(G,pos,)
	plt.show()