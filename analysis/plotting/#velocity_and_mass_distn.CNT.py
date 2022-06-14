######################################
# velocity_and_mass_distn.G.py Revision 1.0 [07-15-2020]
#
# Changelog:
# V1.0 [07-15-2020]
# Initial commit.
######################################

# Compute the velocity and mass distributions on CNTs.

import numpy as np
import pandas as pd
import os

adsorbate = os.getcwd().split('/')[4]
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

max_lx_dict = {
    "CNT10a": 50,
    "CNT15a": 60,
    "CNT20a": 70,
    "CNT10z": 50,
    "CNT15z": 60,
    "CNT20z": 70.   
}

diameter = diameter_dict[surface]
max_lx = max_lx_dict[surface]
adsorbate_index = {
    "DA" : 31,
    "DAH": 33,
    "DOQ": 29,
    "DOQH": 31,
    "Adatom": 10,
    "Ag": 10,
}

water_index = {
    "graphene": 24585,   # 32*32*(4+4) = 8192;      8192*3+9 = 24585
    "CNT10a": 22869,     # 708 + 12*12*48 = 7620;   7620*3+9 = 22869
    "CNT15a": 33576,     # 1781 + 14*14*48 = 11189; 11189*3+9 = 33576
    "CNT20a": 46443,     # 3190 + 16*16*48 = 15748; 15748*3+9 = 46443
    "CNT10z": 22914,     # 723 + 12*12*48 = 7635;   7635*3+9 = 22914
    "CNT15z": 33624,     # 1797 + 14*14*48 = 11205; 11205*3+9 = 33624
    "CNT20z": 47415,     # 3514 + 16*16*48 = 15802; 15802*3+9 = 47415
}

def logic(index):
    if index % water_index[surface] < 9:
       return True
    return False

lx_line = 13
ly_line = 14

center_x = max_lx/2
center_y = max_lx/2

bins = np.arange(0,max_lx/2,0.01)
avgVelocity = np.zeros(len(bins))
vx = np.zeros(len(bins))
vy = np.zeros(len(bins))
vz = np.zeros(len(bins))
vr = np.zeros(len(bins))
vrtheta = np.zeros(len(bins))
avgWaterMass = np.zeros(len(bins))

for i in range(10):
    print(i)
    filename = str(i) + '/waterVelocity.txt'

    df = pd.read_csv(filename, delimiter = ' ', \
                     skiprows= lambda x: logic(x), \
                     names = ['x', 'y', 'z', \
                              'vx', 'vy', 'vz', \
                              'mass', 'None'], \
                     header = None)
    with open(str(i) + '/after_nvt.data', "r") as f:
        for j, line in enumerate(f):
            if j == lx_line:
                lx = np.float(line.split(' ')[1]) - np.float(line.split(' ')[0])
            if j == ly_line:
                ly = np.float(line.split(' ')[1]) - np.float(line.split(' ')[0])

    df['wrapped_x'] = df['x']%lx
    df['wrapped_y'] = df['y']%ly     

    df['r'] = np.sqrt( (df['wrapped_x']-center_x)**2 + (df['wrapped_y']-center_y)**2 )
    df['v'] = np.sqrt(df['vx']**2 + df['vy']**2 + df['vz']**2)
    df['theta'] = np.arctan2((df['wrapped_y'] - center_y),(df['wrapped_x'] - center_x))

    df['vr'] = df['vx'] * np.sin(df['theta']) - \
               df['vy'] * np.cos(df['theta'])
    df['vrtheta'] = df['vx'] * np.cos(df['theta']) + \
                    df['vy'] * np.sin(df['theta'])
    for j in range(len(bins)-1):
        values = np.logical_and(df['r']< bins[j+1], df['r']>=bins[j])
        avgVelocity[j] += np.mean(df.loc[values, 'v'])
        vx[j] += np.mean(np.abs(df.loc[values, 'vx']))
        vy[j] += np.mean(np.abs(df.loc[values, 'vy']))
        vz[j] += np.mean(np.abs(df.loc[values, 'vz']))
        vr[j] += np.mean(np.abs(df.loc[values, 'vr']))
        vrtheta[j] += np.mean(np.abs(df.loc[values, 'vrtheta']))
        avgWaterMass[j] += df.loc[values, 'mass'].sum()

avgWaterMass /= bins
avgWaterMass /= np.ma.masked_invalid(avgWaterMass).sum()

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
            if j == lx_line:
                lx = np.float(line.split(' ')[1]) - np.float(line.split(' ')[0])
            if j == ly_line:
                ly = np.float(line.split(' ')[1]) - np.float(line.split(' ')[0])

    df2['wrapped_x'] = df2['x']%lx
    df2['wrapped_y'] = df2['y']%ly   
 
    df2['r'] = np.sqrt( (df2['wrapped_x']-center_x)**2 + (df2['wrapped_y']-center_y)**2 )

    for j in range(len(bins)-1):
        values = np.logical_and(df2['r']<bins[j+1], df2['r']>=bins[j])
        avgDAMass[j] += df2.loc[values, 'mass'].sum()

avgDAMass /= bins
avgDAMass /= np.ma.masked_invalid(avgDAMass).sum()

X = np.array((bins, avgVelocity/10., vx/10., vy/10., vz/10., \
              vr/10., vrtheta/10., avgDAMass, avgWaterMass)).T
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

ax1.plot([diameter_dict[surface]/2, diameter_dict[surface]/2], [0, 0.30],'--k')
ax1.plot(bins, avgVelocity/10., linestyle=linestyle[0], c=cm(.99))
ax3.plot(bins, avgDAMass, linestyle=linestyle[1], c=cm(0))
ax3.plot(bins, avgWaterMass, linestyle=linestyle[0], c=cm(0))
        
from matplotlib.lines import Line2D
ax1.legend([Line2D([0], [0], linestyle=':', color='k', lw=1), \
            Line2D([0], [0], linestyle='-', color='k', lw=1)], \
           ['Water', adsorbate])
ax1.set_xlim((2, max_lx/2-2))
ax1.set_ylim((0,0.04))
ax3.set_ylim((-0.001,0.018))
ax3.spines['left'].set_color(cm(.99))
ax1.tick_params(axis='y', colors=cm(.99))
ax3.spines['right'].set_color(cm(0))
ax3.tick_params(axis='y', colors=cm(0))


plt.savefig('velocity_and_mass_distn.png', dpi=300, bbox_inches='tight')