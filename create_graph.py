# create_graph(coordinates)
from scipy.spatial.distance import pdist, squareform
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from parameters import *

def create_graph(coordinates):
    A = np.array(coordinates)
    B = squareform(pdist(A))
    # print("B=", B)
    G = nx.from_numpy_matrix(B)
    nx.draw_networkx(G, with_edges=False)
    plt.title("Original Graph")
    plt.show()
    for i in range(I):
        for j in range(I):
            if G.get_edge_data(i,j) !=None:
                if (G.get_edge_data(i,j)['weight']>R):
                    # print("i=",i, "j=",j)
                    G.remove_edge(i,j)

    analyze_graph(G) # function below

    
def analyze_graph(G):
    nx.draw_networkx(G, with_labels = True)
    plt.title("Final Graph")
    plt.show()
    print("nodes=", G.number_of_nodes(), "edges=", G.number_of_edges())
    
    # for i in range(I):
    #     for j in range(I):
            # print( "i=",i,"j=",j,G.get_edge_data(i,j))
