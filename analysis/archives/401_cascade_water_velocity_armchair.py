#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 12:00:46 2019

@author: qj3fe
"""

# Plot the velocity profiles of water on differently curved carbon surfaces.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

cascade_interval = 0.005

# =============================================================================
# 0. Initialization
# =============================================================================

systems = ('CNT10a_int', 'CNT15a_int', 'CNT20a_int', 'graphene',\
           'CNT20a_ext', 'CNT15a_ext', 'CNT10a_ext')
legends = ('CNT10a$_\\mathrm{int}$', 'CNT15a$_\\mathrm{int}$', 'CNT20a$_\\mathrm{int}$', 'Graphene',\
           'CNT20a$_\\mathrm{ext}$', 'CNT15a$_\\mathrm{ext}$', 'CNT10a$_\\mathrm{ext}$')
cmap_list = (0.99,0.8,0.65,0.5,0.35,0.2,0.0)
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
# 1. Differently curved carbon surfaces.
# =============================================================================
cm = plt.cm.get_cmap('viridis')
# plot_range = (0,9.5)

fig1, ax1 = plt.subplots()
ax1.set_xlabel('Distance from the surface ($\\mathrm{\AA}$)')
ax1.set_ylabel('Water Velocity')

handles = []

for i in range(len(systems)-1, -1, -1):
    surface = systems[i].split('_')[0]
    filename = '../DA/' + systems[i] + '/nvt/velocity_and_mass_distn.out'
    if ('graphene' in systems[i]) or ('boronnitride' in systems[i]): 
        # Flat surfaces.
        df = pd.read_csv(filename, delimiter = ' ', \
                         names = ['bins', 'avgVelocity', 'vx', 'vy', \
                                  'vz', 'avgDAMass', 'avgWaterMass'], \
                         header = None)
        ax1.plot(df['bins'][:-1], df['avgVelocity'][:-1]-cascade_interval*i, linestyle=linestyle[i], \
                 c=cm(cmap_list[i]))
        line, = ax1.plot(-df['bins'][:-1], df['avgVelocity'][:-1]-cascade_interval*i, linestyle=linestyle[i], \
                 c=cm(cmap_list[i]), label = legends[i])
        handles.append(line)
    elif ('ext' in systems[i]): # on the exterior.
        df = pd.read_csv(filename, delimiter = ' ', \
                         names = ['bins', 'avgVelocity', 'vx', 'vy', \
                                  'vz', 'vr', 'vrtheta', 'avgDAMass', \
                                  'avgWaterMass'], \
                         header = None)
        line, = ax1.plot(df['bins'][:-1]-diameter_dict[surface]/2, df['avgVelocity'][:-1]-cascade_interval*i, \
                 linestyle=linestyle[i], c=cm(cmap_list[i]), label = legends[i])
        handles.append(line)
    elif ('int' in systems[i]): # reverse water velocity profiles if on the interior.
        df = pd.read_csv(filename, delimiter = ' ', \
                         names = ['bins', 'avgVelocity', 'vx', 'vy', \
                                  'vz', 'vr', 'vrtheta', 'avgDAMass', \
                                  'avgWaterMass'], \
                         header = None)
        line, = ax1.plot(-( df['bins'][:-1]-diameter_dict[surface]/2 ), df['avgVelocity'][:-1]-cascade_interval*i, \
                 linestyle=linestyle[i], c=cm(cmap_list[i]), label = legends[i])
        handles.append(line)

# ax1.set_xlim((plot_range[0], plot_range[1]))
ylo, yhi = ax1.get_ylim()

ax1.plot((0,0), ax1.get_ylim(), '--k')
ax1.set_ylim((ylo,yhi))
ax1.set_yticklabels([])
ax1.set_yticks([])

box = ax1.get_position()
ax1.set_position([box.x0, box.y0, box.width*0.85, box.height])
ax1.legend(handles[::-1], legends, loc='center left', bbox_to_anchor=(1, 0.5))

fig1.savefig('../images/401_cascade_water_velocity_armchair.png', dpi=300, bbox_inches='tight')