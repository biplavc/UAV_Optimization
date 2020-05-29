import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from create_graph import *
from create_graph_1 import *

from path_loss_probability import *
from itertools import product  


from parameters import *

random.seed(3)

# user locations
def initialize_area():
    for I in users:
        # I is number of users, L length and B breadth
        x_vals = random.sample(range(1, L-1), I) # x-coordinates for users
        y_vals = random.sample(range(1, B-1), I) # y-coordinates for users
        z_vals = [0]*I

        user_coordinates = list(zip(x_vals,y_vals))

        x_grid_nos =(L/R) + 1 # number of different values the grid takes for x axis
        y_grid_nos = (B/R) + 1 # number of different values the grid takes for y axis

        grid_x = np.linspace(0, L, num = x_grid_nos) # generate evenly spaced x positions for grid
        grid_y = np.linspace(0, B, num = y_grid_nos) # generate evenly spaced y positions for grid
 
        grid_coordinates = list(product(grid_x , grid_y)) 

        x_points = [x[0] for x in grid_coordinates]
        y_points = [x[1] for x in grid_coordinates]

        # fig, ax1 = plt.subplots()

        # plt.scatter(x_vals, y_vals, label = 'user positions')
        # plt.scatter(x_points, y_points, label = 'drone deployment positions')
        # plt.xlabel("X-axis (m)")
        # plt.ylabel("Y-axis (m)")
        # plt.legend(loc='best', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=False, ncol=4)

        drones_needed_random, drones_needed_MDS = create_graph_1(user_coordinates, grid_coordinates) 
        print("drones_needed_random = ", drones_needed_random, "drones_needed_MDS = ", drones_needed_MDS)

        drones_Random.append(drones_needed_random)
        drones_CustomMDS.append(drones_needed_MDS)


    fig, ax1 = plt.subplots()

    ax1.plot(users, drones_Random, 'k', marker='+', label = 'Random with removal')
    ax1.plot(users, drones_CustomMDS, 'g', marker='^', label = 'Custom MDS')

    legend = ax1.legend(loc='best', shadow=False, fontsize='large')
    # plt.xlabel('Simulation Time')
    plt.xlabel('Number of ground users')
    plt.ylabel('Number of drones needed')
    # ax1.set_xticks(T)
    legend.get_frame().set_facecolor('C0')

    plt.grid(True)
    

    plt.show()

if __name__ == '__main__':

    users = [50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900]
    print("users = ", users)
    drones_Random = []
    drones_CustomMDS = []
    initialize_area() 
    # print(path_loss_probability_LOS(100,300)) # format h/r
    # print(SNR_th)

