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

#adsorbate = os.getcwd().split('/')[4]
#surface = os.getcwd().split('/')[5].split('_')[0]

adsorbate = 'DA'
surface = 'graphene'

water_index = {
    "graphene": 24585, # 32*32*(4+4) = 8192; 8192*3+9 = 24585
}

lz_line = 15
electrode_z = 15

# =============================================================================
# 1. Compute the water velocity profile normal to the surface.
# =============================================================================

max_lz = 15

def logic(index):
    if index % water_index[surface] < 9:
       return True
    return False

bins = np.arange(0,max_lz,0.01)
avgWaterVelocity = np.zeros(len(bins))
watervx = np.zeros(len(bins))
watervy = np.zeros(len(bins))
watervz = np.zeros(len(bins))

for i in range(10):
    print(i)
    filename = '/Volumes/Backup/DopaDiff/DA/graphene/nvt/' + str(i) + '/waterVelocity.txt'

    df = pd.read_csv(filename, delimiter = ' ', \
                      skiprows= lambda x: logic(x), \
                      names = ['x', 'y', 'z', 'vx', 'vy', 'vz', 'mass', 'None'], \
                      header = None)
        
    with open('/Users/jiaqz/Desktop/DA/graphene/nvt/' + str(i) + '/after_nvt.data', "r") as f:
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
        avgWaterVelocity[j] += np.mean(df.loc[values, 'v'])
        watervx[j] += np.mean(np.abs(df.loc[values, 'vx']))
        watervy[j] += np.mean(np.abs(df.loc[values, 'vy']))
        watervz[j] += np.mean(np.abs(df.loc[values, 'vz']))

# =============================================================================
# 2. Plot the velocity distributions of water.
# =============================================================================
import matplotlib.pyplot as plt
plt.style.use('science')
fig = plt.figure(figsize=(3.5,3.5))
ax1 = fig.gca()
ax1.set_xlabel('$d$ ($\\mathrm{\AA}$)')
ax1.set_ylabel('$v_\\mathrm{avg}$ ($\\mathrm{\AA}$/fs)')

ax1.plot(bins[:-1], avgWaterVelocity[:-1]/10., '-k', label = '$\\langle v\\rangle$')
ax1.plot(bins[:-1], watervx[:-1]/10., '-r', label = '$\\langle v_x\\rangle$')
ax1.plot(bins[:-1], watervy[:-1]/10., '-g', label = '$\\langle v_y\\rangle$')
ax1.plot(bins[:-1], watervz[:-1]/10., '-b', label = '$\\langle v_z\\rangle$')

# box = ax1.get_position()
# ax1.set_position([box.x0, box.y0, box.width*0.85, box.height])
ax1.legend(loc='center left', frameon=True, bbox_to_anchor=(1, 0.5))
        
ax1.set_xlim((0, 8))
ax1.set_ylim((0.0,0.030))
plt.savefig('water_directional_velocity.png', dpi=300, bbox_inches='tight')