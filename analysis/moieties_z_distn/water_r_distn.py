######################################
# water_r_distn.py Revision 1.1 [07-21-2020]
#
# Changelog:
# V1.1 [07-21-2020]
# Removed plotting feature.
# The plotting feature is moved to a file.
# V1.0 [07-19-2020]
# Initial commit.
######################################

# Generate z distributions of water on CNTs.

# =============================================================================
# 1. Overall COM distribution of DA.
# =============================================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

lx_line = 13
ly_line = 14
interval = 0.01
bins = np.arange(-15,15,interval)

surface = os.getcwd().split('/')[5].split('_')[0]
diameter_dict = {
    "CNT7a": 14.895,
    "CNT10a": 20.311,
    "CNT15a": 29.790,
    "CNT20a": 39.269,
    "CNT7z": 14.854,
    "CNT10z": 20.326,
    "CNT15z": 29.708,
    "CNT20z": 39.871 
}
radius = diameter_dict[surface]/2.
center_dict = {
    "CNT10a": 25,
    "CNT15a": 30,
    "CNT20a": 35,
    "CNT10z": 25,
    "CNT15z": 30,
    "CNT20z": 35, 
}
center = center_dict[surface]
water_index = {
    "graphene": 24585,   # 32*32*(4+4) = 8192;      8192*3+9 = 24585
    "CNT10a": 22869,     # 708 + 12*12*48 = 7620;   7620*3+9 = 22869
    "CNT15a": 33576,     # 1781 + 14*14*48 = 11189; 11189*3+9 = 33576
    "CNT20a": 46443,     # 3190 + 16*16*48 = 15748; 15748*3+9 = 46443
    "CNT10z": 22914,     # 723 + 12*12*48 = 7635;   7635*3+9 = 22914
    "CNT15z": 33624,     # 1797 + 14*14*48 = 11205; 11205*3+9 = 33624
    "CNT20z": 47415,     # 3514 + 16*16*48 = 15802; 15802*3+9 = 47415
}

lz = {
    "CNT10a": 100.698,
    "CNT15a": 100.698,
    "CNT20a": 100.698,
    "CNT10z": 102.096,
    "CNT15z": 102.096, 
    "CNT20z": 102.096,
}

water_r = np.empty(shape=(0,0))
oxygen_r = np.empty(shape=(0,0))
oxygen_v = np.empty(shape=(0,0))
def logic(index):
    if index % water_index[surface] < 9:
       return True
    return False

for j in range(10):
    print(j)
    filename = "/Volumes/Backup/DopaDiff/DA/CNT10a_ext/nvt/" + str(j) + "/waterVelocity.txt"
    df = pd.read_csv(filename, delimiter = ' ', \
                     skiprows= lambda x: logic(x), \
                     names = ['x', 'y', 'z', 'vx', 'vy', 'vz', 'mass', 'None'], \
                     header = None)

    with open(str(j) + '/after_nvt.data', "r") as f:
        for k, line in enumerate(f):
            if k == lx_line:
                lx = np.float(line.split(' ')[1]) - np.float(line.split(' ')[0])
            if k == ly_line:
                ly = np.float(line.split(' ')[1]) - np.float(line.split(' ')[0])

    mask_array = (df['mass']==15.999)
    oxygen_r = np.append(oxygen_r, np.sqrt((df.loc[mask_array, 'x']%lx-center)**2 + \
                                           (df.loc[mask_array, 'y']%ly-center)**2)-radius)
    water_r = np.append(water_r, np.sqrt((df.loc[:, 'x']%lx-center)**2 + \
                                         (df.loc[:, 'y']%ly-center)**2)-radius)
    oxygen_v = np.append(oxygen_v, np.sqrt(df.loc[mask_array, 'vx']**2 + \
                                           df.loc[mask_array, 'vy']**2 + \
                                           df.loc[mask_array, 'vz']**2) )
        
counts_water, _ = np.histogram(water_r, bins)
counts_oxygen, _ = np.histogram(oxygen_r, bins)

average_speed = np.zeros(len(bins)-1)
for k in range(1, len(bins)):
    mask_array = np.logical_and( oxygen_r >= bins[k-1], oxygen_r < bins[k]) 
    average_speed[k-1] = np.mean(oxygen_v[mask_array])

# =============================================================================
# file output.
# =============================================================================

np.savetxt('water_z_distn.txt', \
           np.c_[bins[1:], counts_water/(30*interval*2*np.pi*(bins[1:]+radius)*lz[surface]), \
                 counts_oxygen/(10*interval*2*np.pi*(bins[1:]+radius)*lz[surface]), average_speed])