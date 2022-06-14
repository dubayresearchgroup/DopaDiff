#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 12:00:46 2019

@author: qj3fe
"""

# Plot the number density profiles of water on differently curved carbon surfaces.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

cascade_interval = 10

# =============================================================================
# 0. Initialization
# =============================================================================

systems = ('CNT10a_ext', 'CNT15a_ext', 'CNT20a_ext', 'graphene',\
           'CNT20a_int', 'CNT15a_int', 'CNT10a_int')
legends = ('CNT10a$_\\mathrm{ext}$', 'CNT15a$_\\mathrm{ext}$', 'CNT20a$_\\mathrm{ext}$', 'Graphene',\
           'CNT20a$_\\mathrm{int}$', 'CNT15a$_\\mathrm{int}$', 'CNT10a$_\\mathrm{int}$')
cmap_list = (0,0.2,0.35,0.5,0.65,0.8,0.99)
linestyle = ('-', '-', '-', '-', '-', '-', '-')

cm = plt.cm.get_cmap('viridis')

# =============================================================================
# 1. Differently curved carbon surfaces.
# =============================================================================

functional_groups = ('Water', 'WaterO')

for j in range(len(functional_groups)):
    fig, ax = plt.subplots()
    for i in range(len(systems)):
        filename = '../DA/' + systems[i] + \
            '/nvt/water_z_distn.txt'
        df = pd.read_csv(filename, delimiter = ' ', \
                         names = ['bins', 'Water', 'WaterO'], \
                         header = None)
        side = 1
        if 'int' in systems[i]:
            side = -1

        mask_array = (df['bins'] > -1000)
        if '10' in systems[i]:
            mask_array = np.logical_and( (df['bins']>-10), (df['bins']<14.4) )
        elif '15' in systems[i]:
            mask_array = (df['bins']>-14.5)    
        ax.plot(side*df.loc[mask_array, 'bins'], df.loc[mask_array, functional_groups[j]]+cascade_interval*i, linestyle=linestyle[i], \
                 c=cm(cmap_list[i]), label = legends[i])  
            
    ylo=ax.get_ylim()[0]; yhi=ax.get_ylim()[1];  
    #ax.plot(df['bins'], np.repeat(33+cascade_interval*i,len(df['bins'])), '--r')
    ax.plot([0,0],[ylo,yhi], '--k')
    ax.set_ylim((ylo,yhi))
    #ax.set_xlim((0,10))
    ax.set_ylabel("$\\rho_N$ (nm$^{-3}$)")
    ax.set_xlabel('Distance from the surface ($\\mathrm{\AA}$)')
    
    ax.set_yticklabels([])
    ax.set_yticks([])
    
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width*0.85, box.height])
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    
    plt.savefig('../images/402_cascade_' + functional_groups[j] + '_num_density_armchair.png', \
                dpi=300, bbox_inches='tight')
    plt.close('all')
    

