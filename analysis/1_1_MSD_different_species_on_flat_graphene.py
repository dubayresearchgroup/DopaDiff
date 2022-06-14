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
from mpl_toolkits.axes_grid1.inset_locator import (inset_axes, InsetPosition,
                                                  mark_inset)
plt.style.use('science')

# =============================================================================
# 1. Different species on flat graphene.
# =============================================================================

adsorbates = ('Adatom', 'Ag', 'DA', 'DAH', 'DOQ', 'DOQH')
legends = ('Adatom(DA)', 'Adatom(Ag)', 'DA', 'DAH$^+$', 'DOQ', 'DOQH$^+$')
linestyle = (':', ':', '-', '-', '-', '-')
cmap_list = (0.0, 0.5, 0.0, 0.33, 0.66, 0.99)

cm = plt.cm.get_cmap('viridis')

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, \
    gridspec_kw={'height_ratios': [2.7, 2.7, 2.7]}, \
    figsize=(3.5,4), \
    )

ax1.set_ylabel("MSD$_x$ ($\mathrm{\AA}^2$)")
ax1.set_ylim((0, 10))
ax1.set_xlim((0, 10))
ax2.set_ylabel("MSD$_y$ ($\mathrm{\AA}^2$)")
ax2.set_ylim((0, 10))
ax2.set_xlim((0, 10))
ax3.set_ylabel("MSD$_z$ ($\mathrm{\AA}^2$)")
ax3.set_ylim((0, 1))
ax3.set_xlim((0, 10))
ax3.set_xlabel("Time (ps)")

axins1 = inset_axes(ax1, width="30%", height="30%", loc=2)
axins1.tick_params(labelleft=False, labelbottom=False)
axins1.set_xlim((0, .5))
axins1.set_ylim((0, .25))

axins2 = inset_axes(ax2, width="30%", height="30%", loc=2)
axins2.tick_params(labelleft=False, labelbottom=False)
axins2.set_xlim((0, .5))
axins2.set_ylim((0, .25))

axins3 = inset_axes(ax3, width="30%", height="30%", loc=2)
axins3.tick_params(labelleft=False, labelbottom=False)
axins3.set_xlim((0, .5))
axins3.set_ylim((0, .25))

mark_inset(ax1, axins1, loc1=2, loc2=4, fc="none", ec='0.5')
mark_inset(ax2, axins2, loc1=2, loc2=4, fc="none", ec='0.5')
mark_inset(ax3, axins3, loc1=2, loc2=4, fc="none", ec='0.5')

ax1.set_xticklabels([])
ax2.set_xticklabels([])

for i in range(len(adsorbates)):
    filename = '../' + adsorbates[i] + '/graphene/nvt/msd_vacf_10.out'
    df = pd.read_csv(filename, delimiter = ' ', \
                     names = ['bins', 'Dx', 'Dy', 'Dz', \
                              'vacfx', 'vacfy', 'vacfz'], \
                     header = None)

    ax1.plot(df['bins'], df['Dx'], linestyle=linestyle[i], \
             c=cm(cmap_list[i]), label = adsorbates[i])
    axins1.plot(df['bins'], df['Dx'], linestyle=linestyle[i], \
                c=cm(cmap_list[i]), label = adsorbates[i])
    ax2.plot(df['bins'], df['Dy'], linestyle=linestyle[i], \
             c=cm(cmap_list[i]), label = adsorbates[i])
    axins2.plot(df['bins'], df['Dy'], linestyle=linestyle[i], \
                c=cm(cmap_list[i]), label = adsorbates[i])
    ax3.plot(df['bins'], df['Dz'], linestyle=linestyle[i], \
             c=cm(cmap_list[i]), label = adsorbates[i])
    axins3.plot(df['bins'], df['Dz'], linestyle=linestyle[i], \
                c=cm(cmap_list[i]), label = adsorbates[i])

box = ax1.get_position()
ax1.set_position([box.x0, box.y0, box.width*0.85, box.height])
box = ax2.get_position()
ax2.set_position([box.x0, box.y0, box.width*0.85, box.height])
box = ax3.get_position()
ax3.set_position([box.x0, box.y0, box.width*0.85, box.height])
# 
# ax3.legend(legends, loc='center left', bbox_to_anchor=(1.02, 1))

plt.savefig('../images/1_1_msd_flat_graphene.png', \
            dpi=300, bbox_inches='tight')
plt.close()