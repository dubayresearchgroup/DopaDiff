######################################
# water_com_distn_plots.G.py Revision 1.0 [08-08-2020]
#
# Changelog:
# V1.0 [08-08-2020]
# Initial Commit. For Figure 4.19.
######################################

# Generate COM distribution of water on flat pristine graphene within cutoff.

import numpy as np
import os
import pandas as pd

cutoff = 2

x_single = 1.418 * 2 * np.sqrt(3)
y_single = 1.418 * 6
x = np.zeros(0)
y = np.zeros(0)

x_waterO = np.zeros(0)
y_waterO = np.zeros(0)

adsorbate = os.getcwd().split('/')[4]
surface = os.getcwd().split('/')[5].split('_')[0]

water_index = {
    "graphene": 24585, # 32*32*(4+4) = 8192; 8192*3+9 = 24585
}

def logic(index):
    if index % water_index[surface] < 9:
       return True
    return False

lz_line = 15
electrode_z = 15

for j in range(10):
    print(j)
    filename =  str(j) + '/waterVelocity.txt'

    df = pd.read_csv(filename, delimiter = ' ', \
                     skiprows= lambda x: logic(x), \
                     names = ['x', 'y', 'z', 'vx', 'vy', 'vz', 'mass', 'None'], \
                     header = None)
        
    with open(str(j) + '/after_nvt.data', "r") as f:
        for k, line in enumerate(f):
            if k == lz_line:
                lz = np.float(line.split(' ')[1]) - np.float(line.split(' ')[0])
                        
    df['wrapped_z'] = df['z'] - electrode_z
    while (df['wrapped_z'] < 0).sum() or (df['wrapped_z'] > lz).sum():
        df.loc[df['wrapped_z'] < 0, 'wrapped_z'] += lz
        df.loc[df['wrapped_z'] > lz, 'wrapped_z'] -= lz
                
    # Wrap the simulation box.
    x = np.append(x, df.loc[(df['wrapped_z'] - electrode_z)<cutoff, 'x'] % x_single)
    y = np.append(y, df.loc[(df['wrapped_z'] - electrode_z)<cutoff, 'y'] % y_single)
    
    x_waterO = np.append(x_waterO, \
                            df.loc[np.logical_and(df['mass'] == 15.999, \
                                                  (df['wrapped_z'] - electrode_z)<cutoff), \
                                   'x'] % x_single)
    y_waterO = np.append(y_waterO, \
                            df.loc[np.logical_and(df['mass'] == 15.999, \
                                                  (df['wrapped_z'] - electrode_z)<cutoff), \
                                   'y'] % y_single)

import matplotlib.pyplot as plt
plt.style.use('science')

fig, ax = plt.subplots(figsize=(2,3))
cm = plt.cm.get_cmap('Blues')
plt.axis('tight')
plt.axes().set_aspect('equal')
plt.axis([0, x_single, 0, y_single], 'scaled')
plt.xlim(0, x_single)
plt.ylim(0, y_single)
plt.ylabel('$y$/$\mathrm{\AA}$')
plt.xlabel('$x$/$\mathrm{\AA}$')
hist = plt.hist2d(x.flatten(), y.flatten(),
                  bins=(int(50*x_single),int(50*y_single)), cmap=cm)
cbar = plt.colorbar()
plt.clim(0,300)
cbar.set_ticks([0,100,200,300])
cbar.ax.set_title('Counts\n Per Pixel')
#cbar.ax.set_yticklabels(['Low\nDensity', 'High\nDensity'])

for i in [0,3,6]:
    for j in range(3):
        circle = plt.Circle((x_single/2*j, y_single/6*i), radius=0.5, fill=False,
                             edgecolor='grey', linestyle='--', linewidth=1)
        plt.gca().add_patch(circle)
for i in [2,5]:
    for j in range(3):
        circle = plt.Circle((x_single/2*j, y_single/6*i), radius=0.5, fill=False,
                             edgecolor='grey', linestyle='--', linewidth=1)
        plt.gca().add_patch(circle)
for i in [0.5,3.5]:
    for j in [0.5,1.5]:
        circle = plt.Circle((x_single/2*j, y_single/6*i), radius=0.5, fill=False,
                             edgecolor='grey', linestyle='--', linewidth=1)
        plt.gca().add_patch(circle)
for i in [1.5,4.5]:
    for j in [0.5,1.5]:
        circle = plt.Circle((x_single/2*j, y_single/6*i), radius=0.5, fill=False,
                             edgecolor='grey', linestyle='--', linewidth=1)
        plt.gca().add_patch(circle)

plt.plot([x_single/2, x_single/2], [0, y_single], 'k--')
plt.plot([0, x_single], [y_single/2, y_single/2], 'k--')

temp_x = np.array([0,1/4,1/2,3/4,1])
temp_y = np.array([0,1/12,0,1/12,0])
plt.plot(temp_x*x_single, temp_y*y_single, 'k-.', lw=1)

temp_x = np.array([0,1/4,1/2,3/4,1])
temp_y = np.array([1/3,1/4,1/3,1/4,1/3])
plt.plot(temp_x*x_single, temp_y*y_single, 'k-.', lw=1)

temp_x = np.array([0,1/4,1/2,3/4,1])
temp_y = np.array([1/2,7/12,1/2,7/12,1/2])
plt.plot(temp_x*x_single, temp_y*y_single, 'k-.', lw=1)

temp_x = np.array([0,1/4,1/2,3/4,1])
temp_y = np.array([5/6,3/4,5/6,3/4,5/6])
plt.plot(temp_x*x_single, temp_y*y_single, 'k-.', lw=1)

temp_x = np.array([1/4,1/4,1/2,1/2,1/4,1/4])
temp_y = np.array([1/12,1/4,1/3,1/2,7/12,3/4])
plt.plot(temp_x*x_single, temp_y*y_single, 'k-.', lw=1)

temp_x = np.array([3/4,3/4,1/2,1/2,3/4,3/4])
temp_y = np.array([1/12,1/4,1/3,1/2,7/12,3/4])
plt.plot(temp_x*x_single, temp_y*y_single, 'k-.', lw=1)

plt.savefig("3_water_com_distn_plot.png", dpi=300, bbox_inches='tight')
plt.close("all")

# =============================================================================
# 
# =============================================================================

fig, ax = plt.subplots(figsize=(2,3))
cm = plt.cm.get_cmap('Blues')
plt.axis('tight')
plt.axes().set_aspect('equal')
plt.axis([0, x_single, 0, y_single], 'scaled')
plt.xlim(0, x_single)
plt.ylim(0, y_single)
plt.ylabel('$y$/$\mathrm{\AA}$')
plt.xlabel('$x$/$\mathrm{\AA}$')
hist = plt.hist2d(x_waterO.flatten(), y_waterO.flatten(),
                  bins=(int(50*x_single),int(50*y_single)), cmap=cm)
cbar = plt.colorbar()
plt.clim(0,100)
cbar.set_ticks([0,25,50,75,100])
cbar.ax.set_title('Counts\n Per Pixel')
#cbar.ax.set_yticklabels(['Low\nDensity', 'High\nDensity'])

for i in [0,3,6]:
    for j in range(3):
        circle = plt.Circle((x_single/2*j, y_single/6*i), radius=0.5, fill=False,
                             edgecolor='grey', linestyle='--', linewidth=1)
        plt.gca().add_patch(circle)
for i in [2,5]:
    for j in range(3):
        circle = plt.Circle((x_single/2*j, y_single/6*i), radius=0.5, fill=False,
                             edgecolor='grey', linestyle='--', linewidth=1)
        plt.gca().add_patch(circle)
for i in [0.5,3.5]:
    for j in [0.5,1.5]:
        circle = plt.Circle((x_single/2*j, y_single/6*i), radius=0.5, fill=False,
                             edgecolor='grey', linestyle='--', linewidth=1)
        plt.gca().add_patch(circle)
for i in [1.5,4.5]:
    for j in [0.5,1.5]:
        circle = plt.Circle((x_single/2*j, y_single/6*i), radius=0.5, fill=False,
                             edgecolor='grey', linestyle='--', linewidth=1)
        plt.gca().add_patch(circle)

plt.plot([x_single/2, x_single/2], [0, y_single], 'k--')
plt.plot([0, x_single], [y_single/2, y_single/2], 'k--')

temp_x = np.array([0,1/4,1/2,3/4,1])
temp_y = np.array([0,1/12,0,1/12,0])
plt.plot(temp_x*x_single, temp_y*y_single, 'k-.', lw=1)

temp_x = np.array([0,1/4,1/2,3/4,1])
temp_y = np.array([1/3,1/4,1/3,1/4,1/3])
plt.plot(temp_x*x_single, temp_y*y_single, 'k-.', lw=1)

temp_x = np.array([0,1/4,1/2,3/4,1])
temp_y = np.array([1/2,7/12,1/2,7/12,1/2])
plt.plot(temp_x*x_single, temp_y*y_single, 'k-.', lw=1)

temp_x = np.array([0,1/4,1/2,3/4,1])
temp_y = np.array([5/6,3/4,5/6,3/4,5/6])
plt.plot(temp_x*x_single, temp_y*y_single, 'k-.', lw=1)

temp_x = np.array([1/4,1/4,1/2,1/2,1/4,1/4])
temp_y = np.array([1/12,1/4,1/3,1/2,7/12,3/4])
plt.plot(temp_x*x_single, temp_y*y_single, 'k-.', lw=1)

temp_x = np.array([3/4,3/4,1/2,1/2,3/4,3/4])
temp_y = np.array([1/12,1/4,1/3,1/2,7/12,3/4])
plt.plot(temp_x*x_single, temp_y*y_single, 'k-.', lw=1)

plt.savefig("3_waterO_com_distn_plot.png", dpi=300, bbox_inches='tight')
plt.close("all")

