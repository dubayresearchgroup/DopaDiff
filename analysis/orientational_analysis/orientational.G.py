######################################
# orientational.G.py Revision 1.0 [07-28-2020]
#
# Changelog:
# V1.0 [07-28-2020]
# Initial commit.
######################################

# =============================================================================
# 1. Orientational Analysis on flat graphene.
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt
import os

data_file_header = 23
data_file_footer = 36
bins = np.linspace(-np.pi, np.pi, 1000)

counts_phi = 0; counts_theta = 0

for j in range(10):
    print(j)
    filename = str(j) + "/data.out"
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
    
    d = np.sqrt( (c7x-c2x)**2 + (c7y-c2y)**2 + (c7z-c2z)**2 )
    phi = np.arcsin( (c7z-c2z)/d )
    theta = np.arctan2( c7x-c2x, c7y-c2y )

    temp_counts_phi, _ = np.histogram(phi, bins)
    temp_counts_theta, _ = np.histogram(theta, bins)
    counts_phi += temp_counts_phi
    counts_theta += temp_counts_theta

np.savetxt('orientational_distn.txt', np.c_[bins[1:], \
                                            counts_phi/counts_phi.sum(), \
                                            counts_theta/counts_theta.sum()])