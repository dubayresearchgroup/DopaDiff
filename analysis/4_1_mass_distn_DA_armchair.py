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

systems = ('CNT10a_ext', 'CNT15a_ext', 'CNT20a_ext', 'graphene',\
           'CNT20a_int', 'CNT15a_int', 'CNT10a_int')
legends = ('CNT10a$_\\mathrm{int}$', 'CNT15a$_\\mathrm{int}$', 'CNT20a$_\\mathrm{int}$', 'Graphene',\
           'CNT20a$_\\mathrm{ext}$', 'CNT15a$_\\mathrm{ext}$', 'CNT10a$_\\mathrm{ext}$')
cmap_list = (0,0.2,0.35,0.5,0.65,0.8,0.99)
linestyle = ('-', '-', '-', '-', '-', '-', '-')

diameter_dict = {
    "CNT7a": 14.895,
    "CNT10a": 20.311,
    "CNT15a": 29.790,
    "CNT20a": 39.269,
    "CNT7z": 14.854,
    "CNT10z": 20.326,
    "CNT15z": 29.708,
    "CNT20z": 39.871 
}

# =============================================================================
# 1. Different species on flat graphene.
# =============================================================================
cm = plt.cm.get_cmap('viridis')
plot_range = (-9.5,9.5)

fig1, ax1 = plt.subplots()
ax1.set_xlabel('Distance from the surface ($\\mathrm{\AA}$)')
ax1.set_ylabel('$v_\mathrm{avg}$ ($\\mathrm{\AA}$/fs)')

fig2, ax2 = plt.subplots()
ax2.set_xlabel('Distance from the surface ($\\mathrm{\AA}$)')
ax2.set_ylabel('Water Mass Distribution')

fig3, ax3 = plt.subplots()
ax3.set_xlabel('Distance from the surface ($\\mathrm{\AA}$)')
ax3.set_ylabel('DA Mass Distribution')

for i in range(len(systems)):
    surface = systems[i].split('_')[0]
    filename = '../DA/' + systems[i] + '/nvt/velocity_and_mass_distn.out'
    if ('graphene' in systems[i]) or ('boronnitride' in systems[i]): 
        # Flat surfaces.
        df = pd.read_csv(filename, delimiter = ' ', \
                         names = ['bins', 'avgVelocity', 'vx', 'vy', \
                                  'vz', 'avgDAMass', 'avgWaterMass'], \
                         header = None)
        ax1.plot(df['bins'][:-1], df['avgVelocity'][:-1]+0.000*i, linestyle=linestyle[i], \
                 c=cm(cmap_list[i]))
        ax1.plot(-df['bins'][:-1], df['avgVelocity'][:-1]+0.000*i, linestyle=linestyle[i], \
                 c=cm(cmap_list[i]), label = legends[i])
        ax2.plot(df['bins'][:-1], df['avgWaterMass'][:-1]/2, linestyle=linestyle[i], \
                  c=cm(cmap_list[i]))
        ax2.plot(-df['bins'][:-1], df['avgWaterMass'][:-1]/2, linestyle=linestyle[i], \
                  c=cm(cmap_list[i]), label = legends[i])
        ax3.plot(df['bins'][:-1], df['avgDAMass'][:-1], linestyle=linestyle[i], \
                  c=cm(cmap_list[i]))
        ax3.plot(-df['bins'][:-1], df['avgDAMass'][:-1], linestyle=linestyle[i], \
                  c=cm(cmap_list[i]), label = legends[i])
    else: # CNTs or BNNTs.
        df = pd.read_csv(filename, delimiter = ' ', \
                         names = ['bins', 'avgVelocity', 'vx', 'vy', \
                                  'vz', 'vr', 'vrtheta', 'avgDAMass', \
                                  'avgWaterMass'], \
                         header = None)
        ax1.plot(df['bins'][:-1]-diameter_dict[surface]/2, df['avgVelocity'][:-1]+0.000*i, \
                 linestyle=linestyle[i], c=cm(cmap_list[i]), label = legends[i])
        ax2.plot(df['bins'][:-1]-diameter_dict[surface]/2, df['avgWaterMass'][:-1], \
                  linestyle=linestyle[i], c=cm(cmap_list[i]), label = legends[i])
        ax3.plot(df['bins'][:-1]-diameter_dict[surface]/2, df['avgDAMass'][:-1], \
                  linestyle=linestyle[i], c=cm(cmap_list[i]), label = legends[i])

ax1.set_xlim((plot_range[0], plot_range[1]))
#ax2.set_xlim((plot_range[0], plot_range[1]))
ax3.set_xlim((plot_range[0], plot_range[1]))
ax1.set_ylim((0, 0.035))
ax2.set_ylim((0, 0.0025))
ax3.set_ylim((0, 0.015))

ax1.plot((0,0), ax1.get_ylim(), '--k')
ax2.plot((0,0), ax2.get_ylim(), '--k')
ax3.plot((0,0), ax3.get_ylim(), '--k')

box = ax1.get_position()
ax1.set_position([box.x0, box.y0, box.width*0.85, box.height])
ax1.legend(loc='center left', frameon=True, bbox_to_anchor=(1, 0.5))
box = ax2.get_position()
ax2.set_position([box.x0, box.y0, box.width*0.85, box.height])
ax2.legend(loc='center left', frameon=True, bbox_to_anchor=(1, 0.5))
box = ax3.get_position()
ax3.set_position([box.x0, box.y0, box.width*0.85, box.height])
ax3.legend(loc='center left', frameon=True, bbox_to_anchor=(1, 0.5))

fig1.savefig('../images/4_1_velocity_profile.png', dpi=300, bbox_inches='tight')
#fig2.savefig('../images/4_2_water_mass_distn.png', dpi=300, bbox_inches='tight')
fig3.savefig('../images/4_1_mass_distn_DA_armchair.png', dpi=300, bbox_inches='tight')