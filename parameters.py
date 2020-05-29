'''
Initialize constants.
All values in SI unless specified
Unverified values have been commented with 'REMAINING'

'''

from dB_linear import *

L = 1200 # 1 km, length of whole region in meters
B = 1200 # 1 km, breadth of whole region in meters

# I = 500  # number of users


fc = 2 * 10**9       # carrier frequency. 2 GHz, https://arxiv.org/pdf/1704.04813.pdf page 21
c = 3 * 10**8         # speed of light

n_L = 3 # LOS System loss in dB, https://arxiv.org/pdf/1704.04813.pdf page 21
n_N = 23 # NLOS system loss in dB  " do "


a = 9.61 # environmental parameters for path loss, from https://arxiv.org/pdf/1702.08395.pdf
b = 0.16 
# LOS link probability , will be calculated from path_loss_probability.py

Pt = 0.5 # Drone transmit power in Watt, https://arxiv.org/pdf/1704.04813.pdf  page 21

BW = 10**6 # 1 MHz,  https://arxiv.org/pdf/1704.04813.pdf  page 21

Pn = from_dBm(-170) * BW # Watt, https://arxiv.org/pdf/1704.04813.pdf  page 21

SNR_th = from_dB(10) # https://arxiv.org/pdf/1801.05000.pdf

R = round(20*((2)**0.5), 3) # REMAINING, edge from a vertex a to b exist if distance between i and j < R