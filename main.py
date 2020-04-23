import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from parameters import *

import random
random.seed(42)

# user locations
def initialize_area():
    x_vals = random.sample(range(1, L-1), I)
    y_vals = random.sample(range(1, B-1), I)
    z_vals = [0]*I

    coordinates = list(zip(x_vals,y_vals,z_vals))
    # plt.scatter(*zip(*coordinates))
    plt.scatter(x_vals, y_vals)
    # print(coordinates)
    plt.xlabel("X-axis (m)")
    plt.ylabel("Y-axis (m)")
    plt.title('Simulation Area')
    plt.show()

if __name__ == '__main__':
    initialize_area()

