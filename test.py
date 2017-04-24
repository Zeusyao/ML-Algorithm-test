"""
load from a txt file,
data structure is matrix,
plot graph with networkX.

author: Chuanyu Yao
email:	chuanyuyao123@163.com
"""
"""
test new
"""
"""
test clone and push
"""
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def plot_graph(str)
    graph_np=np.loadtxt(str);
	graph=nx.from_numpy_matrix(graph_np)
	nx.draw(graph)
	plt.show()
	