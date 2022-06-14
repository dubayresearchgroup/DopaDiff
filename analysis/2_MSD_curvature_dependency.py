#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 12:00:46 2019

@author: qj3fe
"""

# Plot the curvature dependent MSDs.

from matplotlib.lines import Line2D
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.axes_grid1.inset_locator import (inset_axes, InsetPosition,
                                                   mark_inset)
plt.style.use('science')

# =============================================================================
# 1. Different species on flat graphene.
# =============================================================================

systems = ('CNT10a_int', 'CNT15a_int', 'CNT20a_int', 'graphene',
           'CNT20a_ext', 'CNT15a_ext', 'CNT10a_ext')
legends = ('CNT10$_\\mathrm{int}$', 'CNT15$_\\mathrm{int}$', 'CNT20$_\\mathrm{int}$', 'Graphene',
           'CNT20$_\\mathrm{ext}$', 'CNT15$_\\mathrm{ext}$', 'CNT10$_\\mathrm{ext}$')
cmap_list = (0.99, 0.8, 0.65, 0.5, 0.35, 0.2, 0.0)
linestyle = ('-', '-', '-', '-', '-', '-', '-')

cm = plt.cm.get_cmap('viridis')

fig = plt.figure(figsize=(5, 4))
ax1 = fig.add_subplot(211)
ax3 = fig.add_subplot(212)

ax1.set_ylabel("MSD$_\perp$ ($\mathrm{\AA}^2$)")
ax1.set_ylim((0, 5))
ax1.set_xlim((0, 10))
ax3.set_ylabel("MSD$_\parallel$ ($\mathrm{\AA}^2$)")
ax3.set_ylim((0, 5))
ax3.set_xlim((0, 10))
ax3.set_xlabel("Time (ps)")

ax1.set_xticklabels([])

axins1 = inset_axes(ax1, width="30%", height="30%", loc=2)
axins1.tick_params(labelleft=False, labelbottom=False)
axins1.set_xlim((0, .5))
axins1.set_ylim((0, .2))

axins3 = inset_axes(ax3, width="30%", height="30%", loc=2)
axins3.tick_params(labelleft=False, labelbottom=False)
axins3.set_xlim((0, .5))
axins3.set_ylim((0, .2))

mark_inset(ax1, axins1, loc1=2, loc2=4, fc="none", ec='0.5')
mark_inset(ax3, axins3, loc1=2, loc2=4, fc="none", ec='0.5')

for i in range(len(systems)):
    filename = '../DA/' + systems[i] + '/nvt/msd_vacf_10.out'
    df = pd.read_csv(filename, delimiter=' ',
                     names=['bins', 'Dx', 'Dy', 'Dz',
                            'vacfx', 'vacfy', 'vacfz'],
                     header=None)

    ax1.plot(df['bins'], df['Dx'], linestyle=linestyle[i],
             c=cm(cmap_list[i]), label=legends[i])
    axins1.plot(df['bins'], df['Dx'], linestyle=linestyle[i],
                c=cm(cmap_list[i]), label=legends[i])
    ax3.plot(df['bins'], df['Dy'], linestyle=linestyle[i],
             c=cm(cmap_list[i]), label=legends[i])
    axins3.plot(df['bins'], df['Dy'], linestyle=linestyle[i],
                c=cm(cmap_list[i]), label=legends[i])

box = ax1.get_position()
ax1.set_position([box.x0, box.y0, box.width*0.85, box.height])
box = ax3.get_position()
ax3.set_position([box.x0, box.y0, box.width*0.85, box.height])

ax3.legend(legends, loc='center left',
           frameon=True, bbox_to_anchor=(1.02, 0.7))
ax1.legend([Line2D([0], [0], linestyle='-', color='k', lw=1),
            Line2D([0], [0], linestyle=':', color='k', lw=1)],
           ['Armchair', 'Zigzag'], loc='center left', frameon=True, bbox_to_anchor=(1.03, 0.3))

# =============================================================================
# 1. Different species on flat graphene.
# =============================================================================

systems = ('CNT10z_int', 'CNT15z_int', 'CNT20z_int', 'graphene',
           'CNT20z_ext', 'CNT15z_ext', 'CNT10z_ext')
cmap_list = (0.99, 0.8, 0.65, 0.5, 0.35, 0.2, 0.0)
linestyle = (':', ':', ':', ':', ':', ':', ':')

for i in range(len(systems)):
    filename = '../DA/' + systems[i] + '/nvt/msd_vacf_10.out'
    df = pd.read_csv(filename, delimiter=' ',
                     names=['bins', 'Dx', 'Dy', 'Dz',
                            'vacfx', 'vacfy', 'vacfz'],
                     header=None)
    if systems[i] == 'graphene':
        columnsTitles = ['bins', 'Dy', 'Dx', 'Dz',
                         'vacfy', 'vacfx', 'vacfz']
        df = df.reindex(columns=columnsTitles)

    ax1.plot(df['bins'], df['Dx'], linestyle=linestyle[i],
             c=cm(cmap_list[i]), label=legends[i])
    axins1.plot(df['bins'], df['Dx'], linestyle=linestyle[i],
                c=cm(cmap_list[i]), label=legends[i])
    ax3.plot(df['bins'], df['Dy'], linestyle=linestyle[i],
             c=cm(cmap_list[i]), label=legends[i])
    axins3.plot(df['bins'], df['Dy'], linestyle=linestyle[i],
                c=cm(cmap_list[i]), label=legends[i])

plt.savefig('../images/2_MSD_curvature_dependency.png',
            dpi=300, bbox_inches='tight')
plt.close('all')
