######################################
# com_distn_plots.CNT.py Revision 1.4 [09-14-2020]
#
# Changelog:
# V1.4      [09-14-2020]
# Added SciencePlots style.
# Specified axes ticks.
# V1.3      [08-23-2020]
# Increase font size by specify figsize.
# V1.2 [07-21-2020]
# Added back the continuous check without zeroing it.
# V1.1 [07-20-2020]
# Bug fix. Separate armchair and zigzag.
# V1.0 [07-15-2020]
# Initial commit.
######################################

# Generate COM distribution on CNTs.

import numpy as np
import os

header = 23
footer = 36
lx_line = 13
ly_line = 14
lz_line = 15

# =============================================================================
surface = os.getcwd().split('/')[5].split('_')[0]

r_list = {
    "CNT10a": 10.1555,
    "CNT10z": 10.163,
    "CNT15a": 14.895,
    "CNT15z": 14.854,
    "CNT20a": 19.6345,
    "CNT20z": 19.9355,
}
r = r_list[surface]

electrode_list = {
    "CNT10a": 25,
    "CNT10z": 25,
    "CNT15a": 30,
    "CNT15z": 30,
    "CNT20a": 35,
    "CNT20z": 35,
}
ref_x = electrode_list[surface]
ref_y = electrode_list[surface]
# =============================================================================

if surface[-1] == 'z':
    x_single = 1.418 * 2 * np.sqrt(3)
    y_single = 1.418 * 6
elif surface[-1] == 'a':
    x_single = 1.418 * 6
    y_single = 1.418 * 2 * np.sqrt(3)
else: exit()

x = np.zeros((10, 500001))
y = np.zeros((10, 500001))

for j in range(10):
    print(j)
    filename = str(j) + "/data.out"
    temp_x, temp_y, temp_z = \
        np.genfromtxt(filename, skip_header=header, skip_footer=footer, \
                      usecols=(1,2,3), unpack=True)
    
    with open(str(j) + '/after_nvt.data', "r") as f:
        for i, line in enumerate(f):
            if i == lx_line:
                lx = np.float(line.split(' ')[1]) - np.float(line.split(' ')[0])
            if i == ly_line:
                ly = np.float(line.split(' ')[1]) - np.float(line.split(' ')[0])
            if i == lz_line:
                lz = np.float(line.split(' ')[1]) - np.float(line.split(' ')[0])
                
    wrapped_x = temp_x%lx
    wrapped_y = temp_y%ly          
    # Cylindrical coordiante changes.
    cutoff = np.pi/2
    theta = np.arctan2((wrapped_y - ref_y),(wrapped_x - ref_x))
    for i in range(theta.size):
        if np.abs(theta[i] - theta[i-1]) > cutoff:
            if theta[i] - theta[i-1] > 0:
                theta[i:] = theta[i:] - 2*np.pi
            else:
                theta[i:] = theta[i:] + 2*np.pi
    # theta = theta - theta[0]
    # Wrap the simulation box.
            
    x[j] = (r*theta) % x_single
    y[j] = temp_z % y_single

import matplotlib.pyplot as plt
plt.style.use('science')

if surface[-1] == 'z':
    fig, ax = plt.subplots(figsize=(2,3))
elif surface[-1] == 'a':
    fig, ax = plt.subplots(figsize=(3,2))
else: exit()

cm = plt.cm.get_cmap('Blues')
plt.axis('tight')
plt.axes().set_aspect('equal')
plt.axis([0, x_single, 0, y_single], 'scaled')
plt.xlim(0, x_single)
plt.ylim(0, y_single)
plt.ylabel('Axial($\parallel$)/$\mathrm{\AA}$')
plt.xlabel('Perpendicular($\perp$)/$\mathrm{\AA}$')
hist = plt.hist2d(x.flatten(), y.flatten(),
                  bins=(int(50*x_single),int(50*y_single)), cmap=cm)
cbar = plt.colorbar()
plt.clim(0,150)
cbar.set_ticks([0,50,100,150])
cbar.ax.set_title('Counts\n Per Pixel')
#cbar.ax.set_yticklabels(['Low\nDensity', 'High\nDensity'])

if surface[-1] == 'z':
    plt.xticks([0,2,4])
    plt.yticks([0,2,4,6,8])
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
    
    plt.plot([x_single/2, x_single/2], [0, y_single], 'k--')
    plt.plot([0, x_single], [y_single/2, y_single/2], 'k--')
    # plt.text(-0.5, -0.6, '0')
    
elif surface[-1] == 'a':
    plt.xticks([0,2,4,6,8])
    plt.yticks([0,2,4])
    for i in [0,1,2]:
        for j in [0,1,3,4,6]:
            circle = plt.Circle((x_single/6*j, y_single/2*i), radius=0.5, fill=False,
                                 edgecolor='grey', linestyle='--', linewidth=1)
            plt.gca().add_patch(circle)
    for i in [0.5,1.5]:
        for j in [1.5,2.5,4.5,5.5]:
            circle = plt.Circle((x_single/6*j, y_single/2*i), radius=0.5, fill=False,
                                 edgecolor='grey', linestyle='--', linewidth=1)
            plt.gca().add_patch(circle)
            
    temp_x = np.array([0,1/6,1/4,5/12,1/2,2/3,3/4,11/12,1])
    temp_y = np.array([0,0,1/4,1/4,0,0,1/4,1/4,0])
    plt.plot(temp_x*x_single, temp_y*y_single, 'k-.', lw=1)

    temp_x = np.array([0,1/6,1/4,5/12,1/2,2/3,3/4,11/12,1])
    temp_y = np.array([1/2,1/2,1/4,1/4,1/2,1/2,1/4,1/4,1/2])
    plt.plot(temp_x*x_single, temp_y*y_single, 'k-.', lw=1)     

    temp_x = np.array([0,1/6,1/4,5/12,1/2,2/3,3/4,11/12,1])
    temp_y = np.array([1/2,1/2,3/4,3/4,1/2,1/2,3/4,3/4,1/2])
    plt.plot(temp_x*x_single, temp_y*y_single, 'k-.', lw=1)      

    temp_x = np.array([0,1/6,1/4,5/12,1/2,2/3,3/4,11/12,1])
    temp_y = np.array([1,1,3/4,3/4,1,1,3/4,3/4,1])
    plt.plot(temp_x*x_single, temp_y*y_single, 'k-.', lw=1)              
    
    plt.plot([x_single/2, x_single/2], [0, y_single], 'k--')
    plt.plot([0, x_single], [y_single/2, y_single/2], 'k--')
    # plt.text(-0.5, -0.6, '0')
    
else: exit()

plt.tight_layout()
plt.savefig("3_com_distn_plot.png", dpi=300)
plt.close("all")