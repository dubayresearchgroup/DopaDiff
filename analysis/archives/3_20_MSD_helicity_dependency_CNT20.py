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

# =============================================================================
# 1. Different species on flat graphene.
# =============================================================================

systems = ('CNT20a_int', 'CNT20z_int', 'graphene',\
           'CNT20a_ext', 'CNT20z_ext')
legends = ('CNT20a$_\\mathrm{int}$', 'CNT20z$_\\mathrm{int}$', 'Graphene',\
           'CNT20a$_\\mathrm{ext}$', 'CNT20z$_\\mathrm{ext}$')
cmap_list = (0.65,0.65,0.5,0.35,0.35)
linestyle = ('-', '--', '-', '-', '--', '-')

cm = plt.cm.get_cmap('viridis')

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax3 = fig.add_subplot(212)

ax1.set_ylabel("MSD$_\perp$ ($\mathrm{\AA}^2$)")
ax1.set_ylim((0, 10))
ax1.set_xlim((0, 10))
ax3.set_ylabel("MSD$_\parallel$ ($\mathrm{\AA}^2$)")
ax3.set_ylim((0, 10))
ax3.set_xlim((0, 10))
ax3.set_xlabel("Time (ps)")

axins1 = inset_axes(ax1, width="30%", height="30%", loc=2)
axins1.tick_params(labelleft=False, labelbottom=False)
axins1.set_xlim((0, .5))
axins1.set_ylim((0, .25))

axins3 = inset_axes(ax3, width="30%", height="30%", loc=2)
axins3.tick_params(labelleft=False, labelbottom=False)
axins3.set_xlim((0, .5))
axins3.set_ylim((0, .25))

mark_inset(ax1, axins1, loc1=2, loc2=4, fc="none", ec='0.5')
mark_inset(ax3, axins3, loc1=2, loc2=4, fc="none", ec='0.5')

for i in range(len(systems)):
    filename = '../DA/' + systems[i] + '/nvt/msd_vacf_10.out'
    df = pd.read_csv(filename, delimiter = ' ', \
                     names = ['bins', 'Dx', 'Dy', 'Dz', \
                              'vacfx', 'vacfy', 'vacfz'], \
                     header = None)

    ax1.plot(df['bins'], df['Dx'], linestyle=linestyle[i], \
             c=cm(cmap_list[i]), label = legends[i])
    axins1.plot(df['bins'], df['Dx'], linestyle=linestyle[i], \
                c=cm(cmap_list[i]), label = legends[i])
    ax3.plot(df['bins'], df['Dy'], linestyle=linestyle[i], \
             c=cm(cmap_list[i]), label = legends[i])
    axins3.plot(df['bins'], df['Dy'], linestyle=linestyle[i], \
                c=cm(cmap_list[i]), label = legends[i])

box = ax1.get_position()
ax1.set_position([box.x0, box.y0, box.width*0.85, box.height])
box = ax3.get_position()
ax3.set_position([box.x0, box.y0, box.width*0.85, box.height])

ax3.legend(legends, loc='center left', bbox_to_anchor=(1, 1))

plt.savefig('../images/3_20_MSD_helicity_dependency_CNT20.png', \
            dpi=300, bbox_inches='tight')
plt.close('all')