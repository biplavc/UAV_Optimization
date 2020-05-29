## new graph where drones can be deployed over the grid points.

from scipy.spatial.distance import pdist, squareform
from networkx import *
from networkx.algorithms.approximation import min_weighted_dominating_set
from random import choice
import collections

# from networkx.algorithms.approximation import dominating_set

import matplotlib.pyplot as plt
import numpy as np
from parameters import *
import random

def create_graph_1(user_coordinates, grid_coordinates):
    A_1 = np.array(grid_coordinates)
    A_2 = np.array(user_coordinates)
    A = np.append(A_1, A_2, axis = 0)
    print(type(A), np.shape(A_1), np.shape(A_2))
    print("A_1 = ", A_1)
    print("A_2 = ", A_2)
    print("A_3 = ", A)
    B = squareform(pdist(A, metric='euclidean'))
    # print("B=", B)
    G = nx.from_numpy_matrix(B)
    position_dict = {} # dict containing all positions of users and grid points
    for i in range(len(A)):
        position_dict[i] = [A[i][0], A[i][1]]

    # remove all links between the grid points so only minimum drones analysed

    grid_start_index = 0 
    grid_end_index = len(grid_coordinates)
    user_start_index = grid_end_index + 1
    user_end_index = len(user_coordinates) + len(grid_coordinates)

    print(grid_start_index, grid_end_index, user_start_index, user_end_index )


    color_map = []
    for node in G:
        if node < grid_end_index:
            color_map.append('yellow')
        else: 
            color_map.append('green')   


    fig, ax1 = plt.subplots()
    nx.draw_networkx(G, pos = position_dict, node_color=color_map, with_labels=True)
    plt.title("Original Graph")
    plt.show()

    G.remove_edges_from(list(G.edges()))
    fig, ax1 = plt.subplots()
    nx.draw_networkx(G, pos = position_dict, node_color=color_map, with_labels=True)
    plt.title("Edge removed Graph")
    plt.show()




