import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from create_graph import *
from path_loss_probability import *

from parameters import *

random.seed(3)

# user locations
def initialize_area():
    for I in users:
        x_vals = random.sample(range(1, L-1), I) # I is number of users, L length and B breadth
        y_vals = random.sample(range(1, B-1), I)
        z_vals = [0]*I

        coordinates = list(zip(x_vals,y_vals,z_vals))
        # plt.scatter(*zip(*coordinates))

        '''
        plt.scatter(x_vals, y_vals)
        # print(coordinates)
        plt.xlabel("X-axis (m)")
        plt.ylabel("Y-axis (m)")
        plt.title('Simulation Area')
        print(np.shape(coordinates))
        

        labels = ["{0}".format(i) for i in range(len(coordinates))]
        for label, x, y in zip(labels, x_vals,y_vals):
            plt.annotate(
            label,
            xy=(x, y), xytext=(-20, 20),
            textcoords='offset points', ha='right', va='bottom',
            bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
            arrowprops=dict(arrowstyle = '-',connectionstyle='arc3,rad=0'))
        # plt.show()


        '''
        custom_val, random_val, ds_val = create_graph(coordinates, x_vals, y_vals, I) 

        # drones_DS = np.append(drones_DS, ds_val)
        # drones_Random = np.append(drones_Random, random_val)
        # drones_CustomMDS = np.append(drones_CustomMDS, custom_val)
        drones_DS.append(ds_val)
        drones_Random.append(random_val)
        drones_CustomMDS.append(custom_val)


    print('drones_DS = ', drones_DS)
    print('drones_Random = ', drones_Random)
    print('drones_CustomMDS = ', drones_CustomMDS)

    fig, ax1 = plt.subplots()

    ax1.plot(users, drones_DS, 'm', marker='D', label = 'default DS')
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
    users = np.array([20, 25, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800])
    drones_DS = []
    drones_Random = []
    drones_CustomMDS = []
    initialize_area() 
    # print(path_loss_probability_LOS(100,300)) # format h/r
    # print(SNR_th)

