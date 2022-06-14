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

systems = ('CNT10a_ext', 'CNT15a_ext', 'CNT20a_ext', 'graphene',\
           'CNT20a_int', 'CNT15a_int', 'CNT10a_int')
legends = ('CNT10a$_\\mathrm{int}$', 'CNT15a$_\\mathrm{int}$', 'CNT20a$_\\mathrm{int}$', 'Graphene',\
           'CNT20a$_\\mathrm{ext}$', 'CNT15a$_\\mathrm{ext}$', 'CNT10a$_\\mathrm{ext}$')
cmap_list = (0,0.2,0.35,0.5,0.65,0.8,0.99)
linestyle = ('-', '-', '-', '-', '-', '-', '-')

cm = plt.cm.get_cmap('viridis')

for raw_flag in [False, True]:

    if raw_flag == True:
        string = ['x', 'y', 'z']
    else:
        string = ['\\perp', '\\parallel', 'r']
    loc = ['x', 'y', 'z']

    fig, axes = plt.subplots(3,1,figsize=(4,4))

    for i in range(len(systems)):
        if raw_flag == True:
            filename = '/Users/jiaqz/Desktop/DA/' + systems[i] + '/nvt/msd_vacf_10_raw.out'
        else:
            filename = '/Users/jiaqz/Desktop/DA/' + systems[i] + '/nvt/msd_vacf_10.out'
        df = pd.read_csv(filename, delimiter = ' ', \
                         names = ['bins', 'Dx', 'Dy', 'Dz', \
                                  'vacfx', 'vacfy', 'vacfz'], \
                         header = None)

        axes[0].plot(df['bins'], df['vacfx'], linestyle=linestyle[i], \
                 c=cm(cmap_list[i]), label = systems[i])
        #axins1.plot(df['bins'], df['Dx'], linestyle=linestyle[i], \
        #            c=cm(cmap_list[i]), label = systems[i])
        axes[1].plot(df['bins'], df['vacfy'], linestyle=linestyle[i], \
                 c=cm(cmap_list[i]), label = systems[i])
        #axins3.plot(df['bins'], df['Dy'], linestyle=linestyle[i], \
        #            c=cm(cmap_list[i]), label = systems[i])
        axes[2].plot(df['bins'], df['vacfz'], linestyle=linestyle[i], \
                 c=cm(cmap_list[i]), label = systems[i])
        #axins3.plot(df['bins'], df['Dy'], linestyle=linestyle[i], \
        #            c=cm(cmap_list[i]), label = systems[i])

    for k in range(len(axes)):
        axes[k].set_ylabel("$C_" + string[k] + "$ ($\mathrm{\AA}^2$/ps$^2$)")
        axes[k].set_ylim((-1, 2))
        axes[k].set_xlim((0, 2))
        axes[k].plot([0,10],[0,0], '--k')
        box = axes[k].get_position()
        axes[k].set_position([box.x0, box.y0, box.width*0.85, box.height])

    axes[0].set_xticklabels([])
    axes[1].set_xticklabels([])
    axes[2].set_xlabel("Time (ps)")

    axes[2].legend(legends, loc='center left', frameon=True, bbox_to_anchor=(1.02, 1.5))


    if raw_flag == True:
        ofilename = '/Users/jiaqz/Desktop/images/6_1_vacf_armchair_short_raw.png'
    else: 
        ofilename = '/Users/jiaqz/Desktop/images/6_1_vacf_armchair_short.png'

    plt.savefig(ofilename, dpi=300, bbox_inches='tight')
plt.close('all')