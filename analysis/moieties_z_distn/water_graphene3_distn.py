######################################
# water_z_distn.py Revision 1.1 [07-21-2020]
#
# Changelog:
# V1.1 [07-21-2020]
# Removed plotting feature.
# The plotting feature is moved to a file.
# V1.0 [07-19-2020]
# Initial commit.
######################################

# Generate z distributions of water on flat pristine graphene.

# =============================================================================
# 1. Overall COM distribution of DA.
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os


lz_line = 15
electrode_z = 15+3.55
interval = 0.01
bins = np.arange(-electrode_z,electrode_z,interval)

size = 500000
z = np.zeros(shape=(4,10*size))

surface = os.getcwd().split('/')[5].split('_')[0]
water_index = {
    "graphene3": 24585, # 32*32*(4+4) = 8192; 8192*3+9 = 24585
}

lx_times_ly = {
    "graphene3":98.2419*97.842
}
def logic(index):
    if index % water_index[surface] < 9:
       return True
    return False

water_z = np.empty(shape=(0,0))
oxygen_z = np.empty(shape=(0,0))
for j in range(10):
    print(j)
    filename = str(j) + "/waterVelocity.txt"
    df = pd.read_csv(filename, delimiter = ' ', \
                     skiprows= lambda x: logic(x), \
                     names = ['x', 'y', 'z', 'vx', 'vy', 'vz', 'mass', 'None'], \
                     header = None)

    with open(str(j) + '/after_nvt.data', "r") as f:
        for k, line in enumerate(f):
            if k == lz_line:
                lz = np.float(line.split(' ')[1]) - np.float(line.split(' ')[0])

    mask_array = (df['mass']==15.999)
    oxygen_z = np.append(oxygen_z, (df.loc[mask_array, 'z'] % lz)-electrode_z)
    water_z = np.append(water_z, (df.loc[:,'z'] % lz)-electrode_z)
    
counts_water, _ = np.histogram(water_z, bins)
counts_oxygen, _ = np.histogram(oxygen_z, bins)

# =============================================================================
# file output.
# =============================================================================

np.savetxt('water_z_distn.txt', \
           np.c_[bins[1:], counts_water/(30*interval*lx_times_ly[surface]), \
                 counts_oxygen/(10*interval*lx_times_ly[surface])])