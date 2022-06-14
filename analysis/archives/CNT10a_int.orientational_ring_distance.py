######################################
# orientational.CNT.py Revision 1.0 [07-28-2020]
#
# Changelog:
# V1.0 [07-28-2020]
# Initial commit.
######################################

# =============================================================================
# 1. Orientational Analysis on CNTs.
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt
import os

data_file_header = 23
data_file_footer = 36
bins = np.linspace(-np.pi, np.pi, 1000)

theta_stats_5 = np.zeros(0)
theta_stats_85 = np.zeros(0)

counts_phi = 0; counts_theta = 0

surface = "CNT10a"
int_flag = -1
    
lx_line = 13
ly_line = 14

center_dict = {
    "CNT10a": 25,
    "CNT10z": 25,
    "CNT15a": 30,
    "CNT15z": 30,
    "CNT20a": 35,
    "CNT20z": 35,
}
electrode_x = center_dict[surface]
electrode_y = center_dict[surface]
ref_x = center_dict[surface]
ref_y = center_dict[surface]
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

for j in range(10):
    print(j)
    filename = "/Users/jiaqz/Desktop/DA/CNT10a_int/nvt/" + str(j) + "/data.out"
    c2x, c2y, c2z = np.genfromtxt(filename, \
                                  skip_header=data_file_header, \
                                  skip_footer=data_file_footer, \
                                  usecols=(16,17,18), \
                                  unpack=True)
    c7x, c7y, c7z = np.genfromtxt(filename, \
                                  skip_header=data_file_header, \
                                  skip_footer=data_file_footer, \
                                  usecols=(19,20,21), \
                                  unpack=True)

    with open("/Users/jiaqz/Desktop/DA/CNT10a_int/nvt/" + str(j) + '/after_nvt.data', "r") as f:
        for i, line in enumerate(f):
            if i == lx_line:
                lx = np.float(line.split(' ')[1]) - np.float(line.split(' ')[0])
            if i == ly_line:
                ly = np.float(line.split(' ')[1]) - np.float(line.split(' ')[0])
            
    for k in range(len(c2x)):
        while c2x[k] < 0:
            c2x[k] += lx; c7x[k] += lx;
        while c2x[k] > lx:
            c2x[k] -= lx; c7x[k] -= lx;
        while c2y[k] < 0:
            c2y[k] += ly; c7y[k] += ly;
        while c2y[k] > ly:
            c2y[k] -= ly; c7y[k] -= ly;
    r2 = np.sqrt( (c2x-electrode_x)**2 + (c2y-electrode_y)**2 )
    r7 = np.sqrt( (c7x-electrode_x)**2 + (c7y-electrode_y)**2 )
    theta2 = np.arctan2(c2y-electrode_y, c2x-electrode_x)
    theta7 = np.arctan2(c7y-electrode_y, c7x-electrode_x)
    
    if theta2[0]-theta7[0] > np.pi:
        theta7 += 2*np.pi
    if theta2[0]-theta7[0] < -np.pi:
        theta7 -= 2*np.pi
    for l in range(1, len(theta2)):
        if theta2[l]-theta2[l-1] > np.pi:
            theta2[l:] -= 2*np.pi
        if theta7[l]-theta7[l-1] > np.pi:
            theta7[l:] -= 2*np.pi
        if theta2[l]-theta2[l-1] < -np.pi:
            theta2[l:] += 2*np.pi
        if theta7[l]-theta7[l-1] < -np.pi:
            theta7[l:] += 2*np.pi
        
    # Vec a: C2-C7, Vec b: C2-C7'.
    a = np.array((c7x-c2x, c7y-c2y, c7z-c2z))
    b = np.array((r2*np.cos(theta7)+electrode_x-c2x, \
                  r2*np.sin(theta7)+electrode_y-c2y, c7z-c2z))
    mode_a = np.linalg.norm(a, axis=0)
    mode_b = np.linalg.norm(b, axis=0)
        
    cosphi = np.zeros(a.shape[1])
    for l in range(len(cosphi)):
        # if l % 1e5 == 0:
        #     print(l)
        cosphi[l] = np.sum(a[:,l]*b[:,l])/(mode_a[l]*mode_b[l])
    
    # d = np.sqrt( (c7x-c2x)**2 + (c7y-c2y)**2 + (c7z-c2z)**2 )
    phi = int_flag*np.arccos( cosphi )
    phi[r7<r2] *= -1
    theta = np.arctan2(c7z-c2z, radius*(theta7-theta2))
    
    # temp_counts_phi, _ = np.histogram(phi, bins)
    # temp_counts_theta, _ = np.histogram(theta, bins)
    # counts_phi += temp_counts_phi
    # counts_theta += temp_counts_theta

    ring_x, ring_y = np.genfromtxt(filename, \
                                  skip_header=data_file_header, \
                                  skip_footer=data_file_footer, \
                                  usecols=(10,11), \
                                  unpack=True)
    wrapped_x = ring_x%lx
    wrapped_y = ring_y%ly      
    ring_r = np.sqrt((wrapped_y - ref_y)**2 + (wrapped_x - ref_x)**2)
    d = np.abs(ring_r-radius)
    theta_stats_5 = np.append(theta_stats_5, \
        d[np.logical_and(theta<(5/180*np.pi), theta>(-5/180*np.pi))])
    theta_stats_85 = np.append(theta_stats_85, \
        d[np.logical_and(theta>(85/180*np.pi), theta<(95/180*np.pi))])

print(theta_stats_5.mean(), theta_stats_5.std())
print(theta_stats_85.mean(), theta_stats_85.std())
