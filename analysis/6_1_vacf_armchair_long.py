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

for raw_flag in [False, True]:

    xlim = (0,4e2)
    ylim = (-2e-2,2e-2)

    cm = plt.cm.get_cmap('viridis')

    if raw_flag == True:
        string = ['x', 'y', 'z']
    else:
        string = ['\\perp', '\\parallel', 'r']
    loc = ['x', 'y', 'z']

    for k in range(3):

        fig, axes = plt.subplots(7, sharex=True, sharey=True, gridspec_kw={'hspace': 0}, figsize=(3,4))
        handles = []

        for i in range(len(systems)):
            if raw_flag == True:
                filename = '/Users/jiaqz/Desktop/DA/' + systems[i] + '/nvt/msd_vacf_1000_raw.out'
            else:
                filename = '/Users/jiaqz/Desktop/DA/' + systems[i] + '/nvt/msd_vacf_1000.out'
            df = pd.read_csv(filename, delimiter = ' ', \
                             names = ['bins', 'Dx', 'Dy', 'Dz', \
                                      'vacfx', 'vacfy', 'vacfz'], \
                             header = None)

            handles += axes[i].plot(df['bins'], df['vacf' + loc[k]], linestyle=linestyle[i], \
                     c=cm(cmap_list[i]), label = systems[i])
            axes[i].plot(df['bins'], np.zeros(len(df['bins'])), '--k')

        axes[6].set_xlim((xlim))
        axes[6].set_ylim((ylim))
        axes[6].axes.yaxis.set_ticks([-1e-2,0,1e-2])

        axes[6].set_xlabel("Time (ps)")
        axes[6].text(-105, 0.08, "$C_" + string[k] + "$ ($\mathrm{\AA}^2$/ps$^2$)", rotation='vertical')

        if raw_flag == True:
            ofilename = '/Users/jiaqz/Desktop/images/6_1_vacf_armchair_long_' + loc[k] + '_raw.png'
        else:
            ofilename = '/Users/jiaqz/Desktop/images/6_1_vacf_armchair_long_' + loc[k] + '.png'

        plt.savefig(ofilename, dpi=300, bbox_inches='tight')
    plt.close('all')