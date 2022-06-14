#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 12:35:12 2017

@author: jiaqz
"""
# =============================================================================
# Finding the configurations in an NPT trajectory, whose volume is closest to
# the mean value.
# =============================================================================

import shutil 
import numpy as np
import copy
import matplotlib.pyplot as plt

# =============================================================================
# Returns the index of the value is closest to the mean.
# =============================================================================
def find_nearest(array, value):
    idx = (np.abs(array - value)).argmin()
    return idx

path = ''
file_name = 'log.lammps'

header = 562
column_number = (0,6)
footer = 27
num_of_means = 10

vol = np.genfromtxt(file_name, skip_header=header, skip_footer=footer,
                    usecols=(column_number))

mean = np.mean(vol[:,1])

MAX = 1000
tmpvol = copy.deepcopy(vol[:,1])
# ofilename = 'box_sizes.txt'
# f = open(ofilename, 'a+')
for i in range(num_of_means):
    index = find_nearest(tmpvol[:], mean)
    filename = 'restarts/restart.' + str(int(vol[index,0])) + '.dopa'
    destination = '../nvt/restart.' + str(int(vol[index,0])) + '.dopa'
    shutil.copyfile(filename, destination)
#     f.write('{}\t'.format(tmpvol[index]))
    tmpvol[index] = MAX
# f.close()

plt.scatter(vol[:,0]/1000000., vol[:,1], s=5, c='black', linewidths=0)
plt.title("$z$-Dimention in $NPT$ Equilibration")
plt.ylabel("Side Length / $\mathrm{\AA}$")
plt.xlabel("Time / ns")
plt.axvspan(0.25, 1, alpha=0.1, color='k')
plt.xlim([0,1])
plt.ylim([25,35])
plt.savefig('npt.png', dpi=300)
plt.close()