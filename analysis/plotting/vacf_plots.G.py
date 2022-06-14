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
plt.style.use('science')

cmap = plt.cm.get_cmap('Blues')
# =============================================================================
# 2. Component MSD and VACF curves.
# =============================================================================

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, \
    gridspec_kw={'height_ratios': [3.3, 3.3, 3.3]}, \
    figsize=(5,4), \
    )

ax1.set_ylabel("MSD$_x$ ($\mathrm{\AA}^2$)", color=cmap(.75))
ax1.set_ylim((0, 10))
ax1.set_xlim((0, 10))
ax2.set_ylabel("MSD$_y$ ($\mathrm{\AA}^2$)", color=cmap(.75))
ax2.set_ylim((0, 10))
ax2.set_xlim((0, 10))
ax3.set_ylabel("MSD$_z$ ($\mathrm{\AA}^2$)", color=cmap(.75))
ax3.set_ylim((0, 0.1))
ax3.set_xlim((0, 10))
ax3.set_xlabel("Time (ps)")

ax1.set_xticklabels([])
ax2.set_xticklabels([])

axright1 = ax1.twinx()
axright1.set_ylabel("$C_x$ ($\mathrm{\AA}^2$/ps$^2$)", color='r')
axright1.set_ylim((-1.5,2.5))
axright1.set_yticks([-1,0,1,2])
axright2 = ax2.twinx()
axright2.set_ylabel("$C_y$ ($\mathrm{\AA}^2$/ps$^2$)", color='r')
axright2.set_ylim((-1.5,2.5))
axright2.set_yticks([-1,0,1,2])
axright3 = ax3.twinx()
axright3.set_ylabel("$C_z$ ($\mathrm{\AA}^2$/ps$^2$)", color='r')
axright3.set_ylim((-1.5,2.5))
axright3.set_yticks([-1,0,1,2])

axright1.spines['left'].set_color(cmap(.75))
ax1.tick_params(axis='y', colors=cmap(.75))
axright1.spines['right'].set_color('r')
axright1.tick_params(axis='y', colors='r')

axright2.spines['left'].set_color(cmap(.75))
ax2.tick_params(axis='y', colors=cmap(.75))
axright2.spines['right'].set_color('r')
axright2.tick_params(axis='y', colors='r')

axright3.spines['left'].set_color(cmap(.75))
ax3.tick_params(axis='y', colors=cmap(.75))
axright3.spines['right'].set_color('r')
axright3.tick_params(axis='y', colors='r')

filename = 'msd_vacf_10.out'
df = pd.read_csv(filename, delimiter = ' ', \
                 names = ['bins', 'Dx', 'Dy', 'Dz', 'vacfx', 'vacfy', 'vacfz'], \
                 header = None)
ax1.plot(df['bins'], df['Dx'], color=cmap(0.75))
ax2.plot(df['bins'], df['Dy'], color=cmap(0.75))
ax3.plot(df['bins'], df['Dz'], color=cmap(0.75))
axright1.plot(df['bins'], df['vacfx'], color='r', alpha=0.75)
axright2.plot(df['bins'], df['vacfy'], color='r', alpha=0.75)
axright3.plot(df['bins'], df['vacfz'], color='r', alpha=0.75)
axright1.plot([0,10], [0,0], color='k', linestyle=':')
axright2.plot([0,10], [0,0], color='k', linestyle=':')
axright3.plot([0,10], [0,0], color='k', linestyle=':')


box = ax1.get_position()
ax1.set_position([box.x0, box.y0, box.width*0.85, box.height])
box = ax2.get_position()
ax2.set_position([box.x0, box.y0, box.width*0.85, box.height])
box = ax3.get_position()
ax3.set_position([box.x0, box.y0, box.width*0.85, box.height])

plt.savefig('2_vacf_plot.png', dpi=300, bbox_inches='tight')