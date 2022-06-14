#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 12:00:46 2019

@author: qj3fe
"""

# Plot the curvature dependent MSDs.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.axes_grid1.inset_locator import (inset_axes, InsetPosition,
                                                  mark_inset)
plt.style.use('science')

# =============================================================================
# 1. Different species on flat graphene.
# =============================================================================

adsorbates = ('DA', 'DAH', 'DOQ', 'DOQH')

systems = ('CNT10a_int', 'graphene', 'CNT10a_ext')
legends = ('CNT10a$_\\mathrm{int}$', 'Graphene', 'CNT10a$_\\mathrm{ext}$')
cmap_list = (0.99,0.5,0.0)
linestyle = ('-', '-', '-', '-', '-', '-', '-')

cm = plt.cm.get_cmap('viridis')

fig, axes = plt.subplots(4, 1, sharex='all', sharey='all', \
                         gridspec_kw={'hspace': 0, 'wspace': 0}, figsize=(3,4))

axes[0].set_ylim((0, 6))
axes[0].set_xlim((0, 10))
axes[0].set_xticks([0,2,4,6,8,10])
#axes[3].xaxis.get_major_ticks()[-1].set_visible(False)
axes[0].set_yticks([0,2,4,6])
fig.text(0.03, 0.5, "MSD$_\perp$ ($\mathrm{\AA}^2$)", ha='center', va='center', rotation='vertical')
fig.text(0.5, 0.03, "Time (ps)", ha='center', va='center')

for k in range(len(adsorbates)):

    axes[k].tick_params(labelleft=True)
    axes[k].yaxis.tick_left()
    axes[k].yaxis.set_label_position("left")

    if k != 0:
        axes[k].yaxis.get_major_ticks()[-1].set_visible(False)

    axins1 = inset_axes(axes[k], width="30%", height="30%", loc=2)
    axins1.tick_params(labelleft=False, labelbottom=False)
    axins1.set_xlim((0, .5))
    axins1.set_ylim((0, .2))

    mark_inset(axes[k], axins1, loc1=2, loc2=4, fc="none", ec='0.5')

    for i in range(len(systems)):
        filename = '/Users/jiaqz/Desktop/' + adsorbates[k] + '/' + systems[i] + '/nvt/msd_vacf_10.out'
        df = pd.read_csv(filename, delimiter = ' ', \
                         names = ['bins', 'Dx', 'Dy', 'Dz', \
                                  'vacfx', 'vacfy', 'vacfz'], \
                         header = None)

        axes[k].plot(df['bins'], df['Dx'], linestyle=linestyle[k], \
                 c=cm(cmap_list[i]), label = legends[i])
        axins1.plot(df['bins'], df['Dx'], linestyle=linestyle[k], \
                    c=cm(cmap_list[i]), label = legends[i])

# axes[3].legend(legends, loc='center left', frameon=True, bbox_to_anchor=(1, 2))

plt.savefig('/Users/jiaqz/Desktop/images/201_MSD_curvature_dependency_1.png', \
            dpi=300, bbox_inches='tight')
plt.close('all')





##################################


fig, axes = plt.subplots(4, 1, sharex='all', sharey='all', \
                         gridspec_kw={'hspace': 0, 'wspace': 0}, figsize=(3,4))

axes[0].set_ylim((0, 6))
axes[0].set_xlim((0, 10))
axes[0].set_xticks([0,2,4,6,8,10])
#axes[3].xaxis.get_major_ticks()[-1].set_visible(False)
axes[0].set_yticks([0,2,4,6])
fig.text(0.03, 0.5, "MSD$_\parallel$ ($\mathrm{\AA}^2$)", ha='center', va='center', rotation='vertical')
fig.text(0.5, 0.03, "Time (ps)", ha='center', va='center')
for k in range(len(adsorbates)):

    axes[k].tick_params(labelright=True)
    axes[k].yaxis.tick_left()
    axes[k].yaxis.set_label_position("left")

    if k != 0:
        axes[k].yaxis.get_major_ticks()[-1].set_visible(False)

    axins3 = inset_axes(axes[k], width="30%", height="30%", loc=2)
    axins3.tick_params(labelleft=False, labelbottom=False)
    axins3.set_xlim((0, .5))
    axins3.set_ylim((0, .2))

    mark_inset(axes[k], axins1, loc1=2, loc2=4, fc="none", ec='0.5')

    for i in range(len(systems)):
        filename = '/Users/jiaqz/Desktop/' + adsorbates[k] + '/' + systems[i] + '/nvt/msd_vacf_10.out'
        df = pd.read_csv(filename, delimiter = ' ', \
                         names = ['bins', 'Dx', 'Dy', 'Dz', \
                                  'vacfx', 'vacfy', 'vacfz'], \
                         header = None)

        axes[k].plot(df['bins'], df['Dy'], linestyle=linestyle[k], \
                 c=cm(cmap_list[i]), label = legends[i])
        axins3.plot(df['bins'], df['Dy'], linestyle=linestyle[k], \
                    c=cm(cmap_list[i]), label = legends[i])

    # box = axes[k,0].get_position()
    # axes[k,0].set_position([box.x0, box.y0, box.width*0.85, box.height])
    # box = axes[k,1].get_position()
    # axes[k,1].set_position([box.x0, box.y0, box.width*0.85, box.height])

axes[3].legend(legends, loc='center left', frameon=True, bbox_to_anchor=(1, 2))

plt.savefig('/Users/jiaqz/Desktop/images/201_MSD_curvature_dependency_2.png', \
            dpi=300, bbox_inches='tight')
plt.close('all')