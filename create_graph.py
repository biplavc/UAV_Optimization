# create_graph(coordinates)
from scipy.spatial.distance import pdist, squareform
from networkx import *
from networkx.algorithms.approximation import min_weighted_dominating_set
# from networkx.algorithms.approximation import dominating_set

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


    analyze_graph(G, position_dict, x_vals, y_vals) # function below

    
def analyze_graph(G, position_dict, x_vals, y_vals):
    # keys = [i for i in range(I)]
    nx.draw_networkx(G, with_labels = True, pos = position_dict)
    plt.title("Final Graph")
    plt.show()
    print("nodes=", G.number_of_nodes(), "edges=", G.number_of_edges())
    
    # for i in range(I):
    #     for j in range(I):
            # print( "i=",i,"j=",j,G.get_edge_data(i,j))
    get_dominating_set(G, x_vals, y_vals)

def get_dominating_set(G, x_vals, y_vals):
    vertices_1 = min_weighted_dominating_set(G)
    vertices_2 = dominating_set(G)

    print("no of chosen vertices with min_weighted_dominating_set are ", len(vertices_1), "and they are ", vertices_1)
    print("no of chosen vertices with dominating_set are ", len(vertices_2), "and they are ", vertices_2)
    # print("weight = ", G.get_edge_data(2,60))
    compare_graph(vertices_1, vertices_2 , x_vals, y_vals)

def compare_graph(vertices_1, vertices_2 , x_vals, y_vals):

    x_new_1 = [x_vals[i] for i in vertices_1]
    y_new_1 = [y_vals[i] for i in vertices_1]

    x_new_2 = [x_vals[i] for i in vertices_2]
    y_new_2 = [y_vals[i] for i in vertices_2]


    a = plt.scatter( x_vals, y_vals, label = 'All users')
    b = plt.scatter( x_new_1, y_new_1, label = 'Selected Users')
    plt.title("Result of min_weighted_dominating_set")
    plt.legend(loc='best', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=False, ncol=4)
    plt.show()

    a = plt.scatter( x_vals, y_vals, label = 'All users')
    b = plt.scatter( x_new_2, y_new_2, label = 'Selected Users')
    plt.title("Result of dominating_set")
    plt.legend(loc='best', bbox_to_anchor=(0.5, -0.05),
        fancybox=True, shadow=False, ncol=4)
    plt.show()

