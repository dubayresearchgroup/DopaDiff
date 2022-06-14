#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 12:00:46 2019

@author: qj3fe
"""

# Plot the MSDs and the VACFs of DA on flat graphene.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
plt.style.use(['science', 'muted'])

# =============================================================================
# 1. Stacked MSD curves.
# =============================================================================

xlim = (0,2)

surface = os.getcwd().split('/')[5].split('_')[0]

if surface == 'graphene' or surface == 'graphene3' or surface == 'groove':
    CNT_counter = 1
else:
    CNT_counter = 2

sides = ['raw', 'transformed']
legends = [['x', 'y', 'z'], \
           ['\\perp', '\\parallel', 'r']]

directions = ['x', 'y', 'z']

cmap = plt.cm.get_cmap('Blues')

for k in range(CNT_counter):
    for i in range(3):
        fig, ax = plt.subplots(figsize=(5,4))
        ax.set_ylabel("C$_" + legends[k][i] + "$ ($\mathrm{\AA}^2$/ps$^2$)")
        ax.set_xlabel("Time (ps)")

        for j in range(10):
            if sides[k] == 'raw':
                if surface == 'groove':
                    filename = str(j) + '/msd_vacf_10.out'
                else:
                    filename = str(j) + '/msd_vacf_10_raw.out'
            else:
                filename = str(j) + '/msd_vacf_10.out'

            df = pd.read_csv(filename, delimiter = ' ', \
                             names = ['bins', 'Dx', 'Dy', 'Dz', 'vacfx', 'vacfy', 'vacfz'], \
                             header = None)
            ax.plot(np.arange(0,10,0.01), df['vacf' + directions[i]], label = str(j))
        ax.plot(np.arange(0,10,0.01), np.zeros(1000), '--k')

        ax.set_xlim(xlim)
        plt.legend(frameon=True, loc='upper right')
        plt.savefig('1_1_vacf_trajs_' + sides[k] + '_' + directions[i] + '.png', dpi=300, bbox_inches='tight')