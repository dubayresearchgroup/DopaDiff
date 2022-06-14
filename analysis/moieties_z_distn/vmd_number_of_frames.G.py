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

target_1 = 3.76
target_2 = 4.98
target_3 = 5.90  
K = 8

lz_line = 15
electrode_z = 15

z = np.zeros(shape=(2,5000010))

data_file_header = 23
data_file_footer = 36
bins = np.arange(1,11,0.01)

for j in range(10):
    print(j)
    filename = str(j) + "/data.out"
    step, temp_amine_z = \
        np.genfromtxt(filename, \
                      skip_header=data_file_header, \
                      skip_footer=data_file_footer, \
                      usecols=(0,9), \
                      unpack=True)
    
    with open(str(j) + '/after_nvt.data', "r") as f:
        for k, line in enumerate(f):
            if k == lz_line:
                lz = np.float(line.split(' ')[1]) - np.float(line.split(' ')[0])
                
    # Wrap the simulation box.
    z[0,j*500001:(j+1)*500001] = step
    z[1,j*500001:(j+1)*500001] = np.abs((temp_amine_z % lz) - electrode_z)
    


arr = z[1,(z[0]%5000==0)]
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