import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from create_graph import *
from path_loss_probability import *

from parameters import *

random.seed(42)

# user locations
def initialize_area():
    x_vals = random.sample(range(1, L-1), I) # I is number of users, L length and B breadth
    y_vals = random.sample(range(1, B-1), I)
    z_vals = [0]*I

    coordinates = list(zip(x_vals,y_vals,z_vals))
    # plt.scatter(*zip(*coordinates))
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
    plt.show()

    create_graph(coordinates) 


if __name__ == '__main__':
    initialize_area()
    # print(path_loss_probability_LOS(1,20))
    # print(SNR_th)

