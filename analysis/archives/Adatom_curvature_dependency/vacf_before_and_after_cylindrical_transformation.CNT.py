#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 12:00:46 2019

@author: qj3fe
"""

# Compute the diffusion coefficients and the VACFs of DA on CNTs.

# Data Source:
# Desktop/DA

data_dir = ('CNT7', 'CNT10', 'CNT15')
chirality = ('a', 'z')
surface = ('_ext', '_int')

import numpy as np
import os

r = (7.427, 7.4475, 10.163, 10.1555, 14.858, 14.879) # CNT10a radius
ref_x = (17.5, 20.0, 25.0)
ref_y = (17.5, 20.0, 25.0)

v0 = 0.
v1 = 0.

for m in range(3):
    for j in range(2):
        for k in range(2):
            for l in range(10):
                filename = 'DA/' + data_dir[m] + chirality[j] + surface[k] + \
                    "/data." + str(l) + ".out"
# =============================================================================
# All length units are in \AA.
#
# 1. Import data and size check.
# =============================================================================
                temp_x, temp_y, temp_z= \
                    np.genfromtxt(filename, skip_header=15, skip_footer=34, \
                                  usecols=(2,3,4), unpack=True)
                vx, vy, vz = \
                    np.genfromtxt(filename, skip_header=15, skip_footer=34, \
                                  usecols=(5,6,7), unpack=True)

# =============================================================================
# 2. Pre-processing and \theta continuation check.
# =============================================================================

                cutoff = np.pi/2
                theta = np.arctan2((temp_y - ref_y[m]),(temp_x - ref_x[m]))

                for i in range(theta.size):
                    if np.abs(theta[i] - theta[i-1]) > cutoff:
                        if theta[i] - theta[i-1] > 0:
                            theta[i:] = theta[i:] - 2*np.pi
                        else:
                            theta[i:] = theta[i:] + 2*np.pi
                theta = theta - theta[0]

# =============================================================================
# 3. Slicing the data string.
# =============================================================================
    # Compute the relative displacement against the top carbon surface.

                vr = vx * np.sin(theta) + vy * np.cos(theta)
                vrtheta = vx * np.cos(theta) - vy * np.sin(theta)

                v0 += np.sqrt(vx ** 2 + vy ** 2 + vz ** 2).mean()
                v1 += np.sqrt(vr ** 2 + vrtheta ** 2 + vz ** 2).mean()

            v0 /= 10.; v1 /= 10.;
            print('{}{}{}&{:.3f}&{:.3f}\\\\hline'.format(data_dir[m], chirality[j], \
                                    surface[k].replace('_', '\_'), v0*1000, v1*1000))
            v0 = 0.; v1 = 0.;