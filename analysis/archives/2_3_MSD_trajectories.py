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
import os
plt.style.use('science')

# ==============================================(t)===============================
# 1. Different species on flat graphene.
# =============================================================================

cm = plt.cm.get_cmap('viridis')

for k in ['armchair', 'zigzag']:

    systems = ('CNT10' + k[0].lower() + '_int', \
               'CNT15' + k[0].lower() + '_int', \
               'CNT20' + k[0].lower() + '_int', \
               'graphene',\
               'CNT20' + k[0].lower() + '_ext', \
               'CNT15' + k[0].lower() + '_ext', \
               'CNT10' + k[0].lower() + '_ext')
    legends = ('CNT10' + k[0].lower() + '$_\\mathrm{int}$', \
               'CNT15' + k[0].lower() + '$_\\mathrm{int}$', \
               'CNT20' + k[0].lower() + '$_\\mathrm{int}$', \
               'Graphene',\
               'CNT20' + k[0].lower() + '$_\\mathrm{ext}$', \
               'CNT15' + k[0].lower() + '$_\\mathrm{ext}$', \
               'CNT10' + k[0].lower() + '$_\\mathrm{ext}$')
    cmap_list = (0.99,0.8,0.65,0.5,0.35,0.2,0.0)
    linestyle = ('-', '-', '-', '-', '-', '-', '-')

    for j in ['perp', 'parallel']:
        fig, ax = plt.subplots()
        
        ax.set_ylabel('MSD$_\\' + j + '$ ($\mathrm{\AA}^2$)')
        ax.set_ylim((0, 7))
        ax.set_xlim((0, 10))
        ax.set_xlabel("Time (ps)")

        axins = inset_axes(ax, width="30%", height="30%", loc=2)
        axins.tick_params(labelleft=False, labelbottom=False)
        axins.set_xlim((0, .5))
        axins.set_ylim((0, .25))

        mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec='0.5')

        for i in range(len(systems)):
            filename = '/Users/jiaqz/Desktop/DA/' + systems[i] + '/nvt/msd_vacf_10.out'
            df = pd.read_csv(filename, delimiter = ' ', \
                             names = ['bins', 'Dperp', 'Dparallel', 'Dz', \
                                      'vacfx', 'vacfy', 'vacfz'], \
                             header = None)
        
            ax.plot(df['bins'], df['D' + j], linestyle=linestyle[i], \
                     c=cm(cmap_list[i]), label = legends[i])
            axins.plot(df['bins'], df['D' + j], linestyle=linestyle[i], \
                        c=cm(cmap_list[i]), label = legends[i])

        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width*0.85, box.height])

        ax.legend(legends, loc='center left', frameon=True, bbox_to_anchor=(1.02, .5))

        plt.savefig('/Users/jiaqz/Desktop/2_3_MSD_trajectory_' + k + '_' + j + '_original.png', \
                    dpi=300, bbox_inches='tight')
        os.system('convert /Users/jiaqz/Desktop/2_3_MSD_trajectory_' + k + '_' + j + '_original.png \
                   -crop +840+0 /Users/jiaqz/Desktop/legend' + k + '_' + j + '.png')        
        os.system('rm /Users/jiaqz/Desktop/2_3_MSD_trajectory_' + k + '_' + j + '_original.png')


# =============================================================================
# 
# =============================================================================
for k in ['armchair', 'zigzag']:

    systems = ('CNT10' + k[0].lower() + '_int', \
               'CNT15' + k[0].lower() + '_int', \
               'CNT20' + k[0].lower() + '_int', \
               'graphene',\
               'CNT20' + k[0].lower() + '_ext', \
               'CNT15' + k[0].lower() + '_ext', \
               'CNT10' + k[0].lower() + '_ext')
    legends = ('CNT10' + k[0].lower() + '$_\\mathrm{int}$', \
               'CNT15' + k[0].lower() + '$_\\mathrm{int}$', \
               'CNT20' + k[0].lower() + '$_\\mathrm{int}$', \
               'Graphene',\
               'CNT20' + k[0].lower() + '$_\\mathrm{ext}$', \
               'CNT15' + k[0].lower() + '$_\\mathrm{ext}$', \
               'CNT10' + k[0].lower() + '$_\\mathrm{ext}$')
    cmap_list = (0.99,0.8,0.65,0.5,0.35,0.2,0.0)
    linestyle = ('-', '-', '-', '-', '-', '-', '-')

    for j in ['perp', 'parallel']:
        fig, ax = plt.subplots()
        
        ax.set_ylabel('MSD$_\\' + j + '$ ($\mathrm{\AA}^2$)')
        ax.set_ylim((0, 7))
        ax.set_xlim((0, 10))
        ax.set_xlabel("Time (ps)")

        axins = inset_axes(ax, width="30%", height="30%", loc=2)
        axins.tick_params(labelleft=False, labelbottom=False)
        axins.set_xlim((0, .5))
        axins.set_ylim((0, .25))

        mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec='0.5')

        for i in range(len(systems)):
            for m in range(10):
                filename = '/Users/jiaqz/Desktop/DA/' + systems[i] + '/nvt/' + str(m) + '/msd_vacf_10.out'
                df = pd.read_csv(filename, delimiter = ' ', \
                                 names = ['bins', 'Dperp', 'Dparallel', 'Dz', \
                                          'vacfx', 'vacfy', 'vacfz'], \
                                 header = None)
            
                ax.plot(df['bins'], df['D' + j], linestyle=linestyle[i], \
                         c=cm(cmap_list[i]), label = legends[i])
                axins.plot(df['bins'], df['D' + j], linestyle=linestyle[i], \
                            c=cm(cmap_list[i]), label = legends[i])

        # box = ax.get_position()
        # ax.set_position([box.x0, box.y0, box.width*0.85, box.height])

        # ax.legend(legends, loc='center left', bbox_to_anchor=(1.02, .5))

        plt.savefig('/Users/jiaqz/Desktop/2_3_MSD_trajectory_' + k + '_' + j + '.png', \
                    dpi=300, bbox_inches='tight')
        os.system('convert /Users/jiaqz/Desktop/2_3_MSD_trajectory_' + k + '_' + j + '.png \
                   -gravity west -extent 1347x759 -gravity east /Users/jiaqz/Desktop/legend' + k + '_' + j + '.png \
                   -composite /Users/jiaqz/Desktop/2_3_MSD_trajectory_' + k + '_' + j + '.png')
        os.system('rm /Users/jiaqz/Desktop/legend' + k + '_' + j + '.png')
        
plt.close('all')