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

    coordinates = list(zip(x_vals,y_vals))
    plt.scatter(*zip(*coordinates))
    plt.show()
    
if __name__ == '__main__':
    initialize_area()

