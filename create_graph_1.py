## new graph where drones can be deployed over the grid points.

from scipy.spatial.distance import pdist, squareform
from networkx import *
from networkx.algorithms.approximation import min_weighted_dominating_set
from random import choice
import collections
import copy
# from networkx.algorithms.approximation import dominating_set

import matplotlib.pyplot as plt
import numpy as np
from parameters import *
import random

def create_graph_1(user_coordinates, grid_coordinates):
    A_1 = np.array(grid_coordinates)
    A_2 = np.array(user_coordinates)
    A = np.append(A_1, A_2, axis = 0)
    # print(type(A), np.shape(A_1), np.shape(A_2))
    # print("A_1 = ", A_1)
    # print("A_2 = ", A_2)
    # print("A_3 = ", A)
    B = squareform(pdist(A, metric='euclidean'))
    # print("B=", B)
    G = nx.from_numpy_matrix(B)
    position_dict = {} # dict containing all positions of users and grid points
    for i in range(len(A)):
        position_dict[i] = [A[i][0], A[i][1]]

    # remove all links between the grid points so only minimum drones analysed

    grid_start_index = 0 
    grid_end_index = len(grid_coordinates) - 1
    user_start_index = grid_end_index + 1
    user_end_index = len(user_coordinates) + len(grid_coordinates) - 1

    print(grid_start_index, grid_end_index, user_start_index, user_end_index )


    color_map = []
    for node in G:
        if node < user_start_index:
            color_map.append('yellow')
        else: 
            color_map.append('green')   


    # fig, ax1 = plt.subplots()
    # nx.draw_networkx(G, pos = position_dict, node_color=color_map, with_labels=True)
    # plt.title("Original Graph")
    # plt.show()

    G.remove_edges_from(list(G.edges()))
    # fig, ax1 = plt.subplots()
    # nx.draw_networkx(G, pos = position_dict, node_color=color_map, with_labels=True)
    # plt.title("Edge removed Graph")
    # plt.show()

    drone_ids = list(np.linspace(grid_start_index, grid_end_index, num = len(grid_coordinates)))
    user_ids = list(np.linspace(user_start_index, user_end_index, num = len(user_coordinates)))

    drone_ids_1 = copy.deepcopy(drone_ids)
    user_ids_1 = copy.deepcopy(user_ids)

    # print('drone ids ', drone_ids )
    # print('user_ids ', user_ids )



    # for i in drone_ids:
    #     for j in user_ids:
    #         print(G.get_edge_data(i,j)) # all node as no edges
    

    for i in range(len(grid_coordinates)):
        for j in range(len(user_coordinates)):
            # print(i, j, grid_coordinates[i], user_coordinates[j])
            distance = ((grid_coordinates[i][0] -  user_coordinates[j][0])**2 + (grid_coordinates[i][1] -  user_coordinates[j][1])**2)**0.5
            # print("grid = ", i, "user = ", j + user_start_index, grid_coordinates[i], user_coordinates[j], distance)
            if distance < R:
                G.add_edge(i, j+user_start_index, weight=distance)
                # print("grid location ", user_coordinates[i], "user location = ", user_coordinates[j])
                # print("distance between ", i," and ", j + user_start_index, "  is ", distance, " so edge added")
            # else:
            #     G.add_edge(i, j+user_start_index, weight=None)


    labels = nx.get_edge_attributes(G,'weight')

    # print("labels = ", labels )

    # fig, ax1 = plt.subplots()

    # plt.xlabel("X-axis (m)")
    # plt.ylabel("Y-axis (m)")
    # nx.draw_networkx_edge_labels(G,position_dict) #,edge_labels=labels)

    # nx.draw_networkx(G, pos = position_dict, node_color=color_map) #, with_labels=True)
    # plt.title("Coverage Plot for '{0}' users with R='{1}'".format(len(user_coordinates), R))    
    # plt.grid()

    J = G.__class__()
    J.add_nodes_from(G)
    J.add_edges_from(G.edges)
    drones_needed_MDS, n = custom_mds(J, drone_ids, user_ids)
    assert (n == 0) # all users have to be removed as removed means under coverage

    H = G.__class__()
    H.add_nodes_from(G)
    H.add_edges_from(G.edges)
    drones_needed_random, m = random_selection(H, drone_ids_1, user_ids_1)
    assert (m == 0) # all users have to be removed as removed means under coverage

    return (drones_needed_random, drones_needed_MDS)

def custom_mds(G, drone_ids, user_ids):
    # print("custom user ids are ", user_ids)
    selected_nodes_list = []
    while (len(user_ids) > 0): # number of users, and it has to be 0 if all users covered
    # print(G.number_of_nodes() - len(drone_ids))
        degree_list = G.degree(drone_ids)
        # print(degree_list) # working correctly
        degree_list = sorted(degree_list, key=lambda x: x[1], reverse = True)
        # print("degree list = ", degree_list) # working correctly
        selected_node = degree_list[0][0] # 1st node in the tuple
        # print("selected node is ", selected_node)
        neigh = list(G.neighbors(selected_node))
        if len(neigh) == 0:
            # print("node ", selected_node, " has no neighbor")
            # selected_nodes_list.append(selected_node)
            # print("remaining users = ", len(user_ids))
            G.remove_node(selected_node) # here this node is removed so that this node is not selected again
            drone_ids.remove(selected_node)
            # print("node ", selected_node, " removed")

        else:
            # print("node ", selected_node, " has neighbors neighbors = ", neigh)
            selected_nodes_list.append(selected_node)
            # print("node ", selected_node, " selected" )
            for i in neigh:
                G.remove_node(i)
                user_ids.remove(i)
                # print("node ", i, " removed")
                # print("remaining users = ", len(user_ids))
            G.remove_node(selected_node)
            drone_ids.remove(selected_node)
            # print("node ", selected_node, " removed")
    
    # print("selected drones for custom MDS are ", selected_nodes_list, " whose length is  ", len(selected_nodes_list))
    return (len(selected_nodes_list), len(user_ids)) #, G.number_of_nodes())

def random_selection(G, drone_ids, user_ids):
    selected_nodes_list = []
    # print("random user ids are ", user_ids)
    while (len(user_ids) > 0): # number of users, and it has to be 0 if all users covered
        selected_node = random.choice(drone_ids) 
        # print("selected node is ", selected_node)
        neigh = list(G.neighbors(selected_node))
        if len(neigh) == 0:
            # print("node ", selected_node, " has no neighbor")
            # selected_nodes_list.append(selected_node) # not covering anyone so not selected
            # print("remaining users = ", len(user_ids))
            G.remove_node(selected_node) # keep in graph but remove from list so that not selected again
            drone_ids.remove(selected_node) 
            # print("node ", selected_node, " removed")

        else:
            # print("node ", selected_node, " has neighbors neighbors = ", neigh)
            selected_nodes_list.append(selected_node)
            # print("node ", selected_node, " selected" )
            for i in neigh:
                G.remove_node(i)
                user_ids.remove(i)
                # print("node ", i, " removed")
                # print("remaining users = ", len(user_ids))
            G.remove_node(selected_node)
            drone_ids.remove(selected_node)
            # print("node ", selected_node, " removed")

    # print("selected drones for random are ", selected_nodes_list, " whose length is  ", len(selected_nodes_list))

    return (len(selected_nodes_list), len(user_ids)) #, G.number_of_nodes())

    
