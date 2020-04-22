'''
Initialize constants.
All values in SI unless specified
Unverified values have been commented with 'REMAINING'

'''

from dB_linear import *

L = 10000 # 10 km, length of whole region in meters
B = 10000 # 10 km, breadth of whole region in meters

I =  50 # number of users

fc = 2 * 10**9       # carrier frequency. 2 GHz, https://arxiv.org/pdf/1704.04813.pdf page 21
c = 3 * 10**8         # speed of light

n_L = 3 # LOS System loss in dB, https://arxiv.org/pdf/1704.04813.pdf page 21
n_N = 23 # NLOS system loss in dB" do "


p_L = 0.5 # LOS link probability , REMAINING
p_N = 1 - p_L # NLOS link probability

Pt = 0.5 # Drone transmit power in Watt, https://arxiv.org/pdf/1704.04813.pdf  page 21

BW = 10**6 # 1 MHz,  https://arxiv.org/pdf/1704.04813.pdf  page 21

Pn = from_dBm(-170) * BW # Watt, https://arxiv.org/pdf/1704.04813.pdf  page 21

# SNR_th = # REMAINING SNR threshold
