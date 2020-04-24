'''
3 functions, one for dB to linear (watts) and the other for dBm to linear

def from_dB(val) - dB to linear
def from_dBm(val) - dBm to linear
def from_linear(val) - linear to dB.

db = 20 * log10(A)

''' 
import control
# import parameters

def from_dB(db_val):
    linear_val = control.db2mag(db_val)
    return linear_val


def from_dBm(dbm_val):
    linear_val = control.db2mag(dbm_val - 30)
    return linear_val

def from_linear(linear_val):
    db_val = control.mag2db(linear_val)
    return db_val

# print(from_dB(20))
# print(from_dBm(20))
# print(from_linear(20))
