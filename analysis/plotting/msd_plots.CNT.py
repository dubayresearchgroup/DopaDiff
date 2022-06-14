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

# =============================================================================
# 1. Stacked MSD curves.
# =============================================================================

fig = plt.figure()
ax = fig.gca()

ax.set_ylabel("MSD ($\mathrm{\AA}^2$)")
ax.set_ylim((0, 15))
ax.set_xlim((0, 10))
ax.set_xlabel("Time (ps)")

cmap = plt.cm.get_cmap('Blues')
filename = 'msd_vacf_10.out'
df = pd.read_csv(filename, delimiter = ' ', \
                 names = ['bins', 'Dx', 'Dy', 'Dz', 'vacfx', 'vacfy', 'vacfz'], \
                 header = None)
ax.fill_between(df['bins'], df['Dx']+df['Dy']+df['Dz'], color=cmap(0.25))
ax.fill_between(df['bins'], df['Dy']+df['Dz'], color=cmap(0.5))
ax.fill_between(df['bins'], df['Dz'], color=cmap(0.75))

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width*0.85, box.height])

ax.legend(['MSD$_\perp$', 'MSD$_\parallel$', 'MSD$_r$'], loc='center left', bbox_to_anchor=(1, 0.5))

plt.savefig('1_msd_plot.png', dpi=300, bbox_inches='tight')