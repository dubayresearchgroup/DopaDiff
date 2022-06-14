######################################
# water_z_directional_velocity.py Revision 1.0 [07-27-2020]
#
# Changelog:
# V1.0 [07-27-2020]
# Initial commit.
######################################

# Compute the directional velocity of water on graphene.

import numpy as np
import pandas as pd
import os

adsorbate = os.getcwd().split('/')[4]
surface = os.getcwd().split('/')[5].split('_')[0]

water_index = {
    "graphene3": 24585, # 32*32*(4+4) = 8192; 8192*3+9 = 24585
}

lz_line = 15
electrode_z = 15+3.55

# =============================================================================
# 1. Compute the water velocity profile normal to the surface.
# =============================================================================

max_lz = 15

def logic(index):
    if index % water_index[surface] < 9:
       return True
    return False

bins = np.arange(0,max_lz+3.55,0.01)
avgWaterVelocity = np.zeros(len(bins))
watervx = np.zeros(len(bins))
watervy = np.zeros(len(bins))
watervz = np.zeros(len(bins))

for i in range(10):
    print(i)
    filename =  str(i) + '/waterVelocity.txt'

    df = pd.read_csv(filename, delimiter = ' ', \
                     skiprows= lambda x: logic(x), \
                     names = ['x', 'y', 'z', 'vx', 'vy', 'vz', 'mass', 'None'], \
                     header = None)
        
    with open(str(i) + '/after_nvt.data', "r") as f:
        for j, line in enumerate(f):
            if j == lz_line:
                lz = np.float(line.split(' ')[1]) - np.float(line.split(' ')[0])
                        
    df['wrapped_z'] = df['z'] - electrode_z
    while (df['wrapped_z'] < 0).sum() or (df['wrapped_z'] > lz).sum():
        df.loc[df['wrapped_z'] < 0, 'wrapped_z'] += lz
        df.loc[df['wrapped_z'] > lz, 'wrapped_z'] -= lz

    mask_array = (df['wrapped_z'] > lz/2)
    df.loc[mask_array, 'wrapped_z'] = lz - df.loc[mask_array, 'wrapped_z']

    df['v'] = np.sqrt(df['vx']**2 + df['vy']**2 + df['vz']**2)
    for j in range(0, len(bins)-1):
        values = np.logical_and(df['wrapped_z']< bins[j+1], df['wrapped_z']>=bins[j])
        watervx[j] += np.mean(np.abs(df.loc[values, 'vx']))
        watervy[j] += np.mean(np.abs(df.loc[values, 'vy']))
        watervz[j] += np.mean(np.abs(df.loc[values, 'vz']))

# =============================================================================
# 2. Plot the velocity distributions of water.
# =============================================================================
import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.gca()
ax1.set_xlabel('Distance ($\\mathrm{\AA}$)')
ax1.set_ylabel('Velocity ($\\mathrm{\AA}/fs$)')

avgWaterVelocity = np.sqrt(watervx**2 + watervy**2 + watervz**2)
ax1.plot(bins[:-1], avgWaterVelocity[:-1]/10., '-k', label = 'v(water)')
ax1.plot(bins[:-1], watervx[:-1]/10., '-r', label = '$v_x$(water)')
ax1.plot(bins[:-1], watervy[:-1]/10., '-g', label = '$v_y$(water)')
ax1.plot(bins[:-1], watervz[:-1]/10., '-b', label = '$v_z$(water)')

box = ax1.get_position()
ax1.set_position([box.x0, box.y0, box.width*0.85, box.height])
ax1.legend(loc='center left', bbox_to_anchor=(1.02, 0.5))
        
ax1.set_xlim((0, 15))
ax1.set_ylim((0,0.035))
plt.savefig('water_directional_velocity.png', dpi=300, bbox_inches='tight')