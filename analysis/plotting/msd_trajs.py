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

surface = os.getcwd().split('/')[5].split('_')[0]

if surface == 'graphene' or surface == 'graphene3' or 'groove' in surface:
    legends = ['x', 'y', 'z']
else:
    legends = ['\\perp', '\\parallel', 'r']

directions = ['x', 'y', 'z']

for i in range(3):
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.set_ylabel("MSD$_" + legends[i] + "$ ($\mathrm{\AA}^2$)")
    ax.set_xlabel("Time (ps)")

    cmap = plt.cm.get_cmap('Blues')

    for j in range(10):
        filename = str(j) + '/msd_vacf_10.out'
        df = pd.read_csv(filename, delimiter=' ',
                         names=['bins', 'Dx', 'Dy', 'Dz',
                                'vacfx', 'vacfy', 'vacfz'],
                         header=None)
        ax.plot(np.arange(0, 10, 0.01), df['D' + directions[i]], label=str(j))

    plt.legend(frameon=True, loc='upper left')
    plt.savefig('1_1_msd_trajs_' +
                directions[i] + '.png', dpi=300, bbox_inches='tight')
