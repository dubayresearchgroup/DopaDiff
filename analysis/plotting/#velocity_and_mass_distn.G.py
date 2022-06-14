######################################
# velocity_and_mass_distn.G.py Revision 1.0 [07-15-2020]
#
# Changelog:
# V1.0 [07-15-2020]
# Initial commit.
######################################

# Compute the velocity and mass distributions on graphene.

import numpy as np
import pandas as pd
import os

adsorbate = os.getcwd().split('/')[4]
surface = os.getcwd().split('/')[5].split('_')[0]

adsorbate_index = {
    "DA" : 31,
    "DAH": 33,
    "DOQ": 29,
    "DOQH": 31,
    "Adatom": 10,
    "Ag": 10,
}

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
avgVelocity = np.zeros(len(bins))
vx = np.zeros(len(bins))
vy = np.zeros(len(bins))
vz = np.zeros(len(bins))
avgWaterMass = np.zeros(len(bins))

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
        avgVelocity[j] += np.mean(df.loc[values, 'v'])
        vx[j] += np.mean(np.abs(df.loc[values, 'vx']))
        vy[j] += np.mean(np.abs(df.loc[values, 'vy']))
        vz[j] += np.mean(np.abs(df.loc[values, 'vz']))
        avgWaterMass[j] += df.loc[values, 'mass'].sum()

avgWaterMass /= avgWaterMass.sum()

# =============================================================================
# 2. Mass distribution of DA.
# =============================================================================

def logic2(index):
    if index % adsorbate_index[adsorbate] < 9:
       return True
    return False

avgDAMass = np.zeros(len(bins))

for i in range(10):
    print(i+10)
    filename = str(i) + '/DAMass.txt'
    df2 = pd.read_csv(filename, delimiter = ' ', \
                      skiprows= lambda x: logic2(x), \
                      names = ['x', 'y', 'z', 'mass', 'None'], \
                      header = None)
    with open(str(i) + '/after_nvt.data', "r") as f:
        for j, line in enumerate(f):
            if j == lz_line:
                lz = np.float(line.split(' ')[1]) - np.float(line.split(' ')[0])
                
    df2['wrapped_z'] = df2['z'] - electrode_z
    while (df2['wrapped_z'] < 0).sum() or (df2['wrapped_z'] > lz).sum():
        df2.loc[df2['wrapped_z'] < 0, 'wrapped_z'] += lz
        df2.loc[df2['wrapped_z'] > lz, 'wrapped_z']  -= lz
    mask_array = (df2['wrapped_z'] > lz/2)
    df2.loc[mask_array, 'wrapped_z'] = lz - df2.loc[mask_array, 'wrapped_z']

    for j in range(0, len(bins)-1):
        values = np.logical_and(df2['wrapped_z']<bins[j+1], df2['wrapped_z']>=bins[j])
        avgDAMass[j] += df2.loc[values, 'mass'].sum()

avgDAMass /= avgDAMass.sum()

X = np.array((bins, avgVelocity/10., vx/10., vy/10., vz/10., avgDAMass, avgWaterMass)).T
np.savetxt('velocity_and_mass_distn.out', X)

# =============================================================================
# 3. Plot the velocity and mass distributions.
# =============================================================================
import matplotlib.pyplot as plt
linestyle = (':', '-')
cm = plt.cm.get_cmap('bwr')
fig = plt.figure()
ax1 = fig.gca()
ax1.set_xlabel('Distance ($\\mathrm{\AA}$)')
ax1.set_ylabel('Velocity ($\\mathrm{\AA}/fs$)')
ax3 = ax1.twinx()
ax3.set_ylabel('Mass Distributions')

ax1.plot(bins, avgVelocity/10., linestyle=linestyle[0], c=cm(.99))
ax3.plot(bins, avgDAMass, linestyle=linestyle[1], c=cm(0))
ax3.plot(bins, avgWaterMass, linestyle=linestyle[0], c=cm(0))
        
from matplotlib.lines import Line2D
ax1.legend([Line2D([0], [0], linestyle=':', color='k', lw=1), \
            Line2D([0], [0], linestyle='-', color='k', lw=1)], \
           ['Water', adsorbate])
ax1.set_xlim((0, 9))
ax1.set_ylim((0,0.04))
ax3.set_ylim((-0.001,0.018))
ax3.spines['left'].set_color(cm(.99))
ax1.tick_params(axis='y', colors=cm(.99))
ax3.spines['right'].set_color(cm(0))
ax3.tick_params(axis='y', colors=cm(0))
plt.savefig('velocity_and_mass_distn.png', dpi=300, bbox_inches='tight')