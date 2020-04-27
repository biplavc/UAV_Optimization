# create_graph(coordinates)
from scipy.spatial.distance import pdist, squareform
import networkx as nx
from networkx.algorithms.approximation import vertex_cover
import matplotlib.pyplot as plt
import numpy as np
from parameters import *

def create_graph(coordinates, x_vals, y_vals):
    A = np.array(coordinates)
    B = squareform(pdist(A, metric='euclidean'))
    # print("B=", B)
    G = nx.from_numpy_matrix(B)
    position_dict = {}
    for i in range(I):
        position_dict[i] = [x_vals[i], y_vals[i]]
    # nx.draw_networkx(G, with_labels = True, pos = position_dict)
    # plt.title("Original Graph")
    plt.show()
    # print("weight = ", G.get_edge_data(2,60))
    for i in range(I):
        for j in range(I):
            if G.get_edge_data(i,j) !=None:
                if (G.get_edge_data(i,j)['weight']>R):
                    # print("i=",i, "j=",j)
                    G.remove_edge(i,j)


    analyze_graph(G, position_dict) # function below

    
def analyze_graph(G, position_dict):
    # keys = [i for i in range(I)]
    nx.draw_networkx(G, with_labels = True, pos = position_dict)
    plt.title("Final Graph")
    plt.show()
    print("nodes=", G.number_of_nodes(), "edges=", G.number_of_edges())
    
    # for i in range(I):
    #     for j in range(I):
            # print( "i=",i,"j=",j,G.get_edge_data(i,j))
    min_vertex_cover(G)

def min_vertex_cover(G):
    vertices = vertex_cover.min_weighted_vertex_cover(G, weight = 'weight')

    print("no of chosen vertices are ", len(vertices), "and they are ", vertices)
    # print("weight = ", G.get_edge_data(2,60))