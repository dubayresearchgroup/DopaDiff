######################################
# water_r_directional_velocity.py Revision 1.0 [07-27-2020]
#
# Changelog:
# V1.0 [07-27-2020]
# Initial commit.
######################################

# Compute the directional velocity of water on CNTs.

import numpy as np
import pandas as pd
import os

#adsorbate = os.getcwd().split('/')[4]
#surface = os.getcwd().split('/')[5].split('_')[0]

adsorbate = 'DA'
surface = 'CNT10a'

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
avgWaterVelocity = np.zeros(len(bins))
watervx = np.zeros(len(bins))
watervy = np.zeros(len(bins))
watervz = np.zeros(len(bins))
watervr = np.zeros(len(bins))
watervrtheta = np.zeros(len(bins))

for i in range(10):
    print(i)
    filename = '/Volumes/Backup/DopaDiff/DA/CNT10a_int/nvt/' + str(i) + '/waterVelocity.txt'

    df = pd.read_csv(filename, delimiter = ' ', \
                     skiprows= lambda x: logic(x), \
                     names = ['x', 'y', 'z', \
                              'vx', 'vy', 'vz', \
                              'mass', 'None'], \
                     header = None)
    with open('/Users/jiaqz/Desktop/DA/CNT10a_int/nvt/' + str(i) + '/after_nvt.data', "r") as f:
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
        avgWaterVelocity[j] += np.mean(df.loc[values, 'v'])
        watervx[j] += np.mean(np.abs(df.loc[values, 'vx']))
        watervy[j] += np.mean(np.abs(df.loc[values, 'vy']))
        watervz[j] += np.mean(np.abs(df.loc[values, 'vz']))
        watervr[j] += np.mean(np.abs(df.loc[values, 'vr']))
        watervrtheta[j] += np.mean(np.abs(df.loc[values, 'vrtheta']))

# =============================================================================
# 2. Plot the velocity distributions of water.
# =============================================================================
import matplotlib.pyplot as plt
plt.style.use('science')
fig = plt.figure(figsize=(3.5,3.5))
ax1 = fig.gca()
ax1.set_xlabel('$d$ ($\\mathrm{\AA}$)')
ax1.set_ylabel('$v_\\mathrm{avg}$ ($\\mathrm{\AA}$/fs)')

# ax1.plot([0,0], [0, 0.30],'--k')
ax1.plot(bins[:-1] - diameter_dict[surface]/2, avgWaterVelocity[:-1]/10., '-k', label = '$\\langle v\\rangle$')
ax1.plot(bins[:-1] - diameter_dict[surface]/2, watervr[:-1]/10., '-r', label = '$\\langle v_r\\rangle$')
ax1.plot(bins[:-1] - diameter_dict[surface]/2, watervrtheta[:-1]/10., '-g', label = '$\\langle v_{\\theta}\\rangle$')
ax1.plot(bins[:-1] - diameter_dict[surface]/2, watervz[:-1]/10., '-b', label = '$\\langle v_z\\rangle$')
        
# box = ax1.get_position()
# ax1.set_position([box.x0, box.y0, box.width*0.85, box.height])
ax1.legend(loc='center left', frameon=True, bbox_to_anchor=(1, 0.5))

ax1.set_xlim((0, 8))
ax1.set_ylim((0.0,0.030))
plt.savefig('water_int_directional_velocity.png', dpi=300, bbox_inches='tight')