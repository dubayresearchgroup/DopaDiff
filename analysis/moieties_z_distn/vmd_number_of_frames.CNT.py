#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 16:02:54 2018

@author: qj3fe
"""

# Generate z distributions of functional groups of DA on flat pristine graphene.
# =============================================================================
# 1. Overall COM distribution of DA.
# =============================================================================
import numpy as np
import os

side = os.getcwd().split('/')[5].split('_')[1]
if 'ext' in side:
    target_1 = 3.18
    target_2 = 4.20
    target_3 = 5.88
elif 'int' in side:
    target_1 = 3.54
    target_2 = 4.85
    target_3 = 5.59
else:
    exit()
K = 8

lx_line = 13
ly_line = 14

r = np.zeros(shape=(2,5000010))

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
radius = diameter_dict[surface]/2.
center_dict = {
    "CNT10a": 25,
    "CNT15a": 30,
    "CNT20a": 35,
    "CNT10z": 25,
    "CNT15z": 30,
    "CNT20z": 35, 
}
center = center_dict[surface]

data_file_header = 23
data_file_footer = 36
bins = np.arange(1,11,0.01)

for j in range(10):
    print(j)
    filename = str(j) + "/data.out"
    step, temp_amine_x, temp_amine_y = \
        np.genfromtxt(filename, \
                      skip_header=data_file_header, \
                      skip_footer=data_file_footer, \
                      usecols=(0,7,8), \
                      unpack=True)

    with open(str(j) + '/after_nvt.data', "r") as f:
        for k, line in enumerate(f):
            if k == lx_line:
                lx = np.float(line.split(' ')[1]) - np.float(line.split(' ')[0])
            if k == ly_line:
                ly = np.float(line.split(' ')[1]) - np.float(line.split(' ')[0])

    # Wrap the simulation box.
    r[0,j*500001:(j+1)*500001] = step
    r[1,j*500001:(j+1)*500001] = np.abs( np.sqrt((temp_amine_x%lx-center)**2 + \
                                                 (temp_amine_y%lx-center)**2) - \
                                        radius)

arr = r[1,(r[0]%5000==0)]
arr_1 = np.abs(arr-target_1)
arr_2 = np.abs(arr-target_2)
arr_3 = np.abs(arr-target_3)

res_1 = sorted(range(len(arr_1)), key = lambda sub: arr_1[sub])[:K] 
print("Indices list of 1st peak is : " + str(res_1)) 
res_2 = sorted(range(len(arr_2)), key = lambda sub: arr_2[sub])[:K] 
print("Indices list of 2nd peak is : " + str(res_2)) 
res_3 = sorted(range(len(arr_3)), key = lambda sub: arr_3[sub])[:K] 
print("Indices list of 3rd peak is : " + str(res_3)) 

print(np.around(arr[res_1],3))
print(np.around(arr[res_2],3))
print(np.around(arr[res_3],3))

ofilename = 'output.txt'
f = open(ofilename, 'w+')
f.write("Indices list of 1st peak is : " + str(res_1) + "\n")
f.write("Indices list of 2nd peak is : " + str(res_2) + "\n")
f.write("Indices list of 3rd peak is : " + str(res_3) + "\n")
f.write("Target\t" + str(target_1) + "\t")
f.write(str(np.around(arr[res_1],3)) + "\n")
f.write("Target\t" + str(target_2) + "\t")
f.write(str(np.around(arr[res_2],3)) + "\n")
f.write("Target\t" + str(target_3) + "\t")
f.write(str(np.around(arr[res_3],3)) + "\n")
f.close()