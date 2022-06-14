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
plt.style.use('science')

# =============================================================================
# 1. Different species on flat graphene.
# =============================================================================

systems = ('CNT10a_ext', 'CNT15a_ext', 'CNT20a_ext', 'graphene',\
           'CNT20a_int', 'CNT15a_int', 'CNT10a_int')
legends = ('CNT10a$_\\mathrm{ext}$', 'CNT15a$_\\mathrm{ext}$', 'CNT20a$_\\mathrm{ext}$',  'Graphene', \
           'CNT20a$_\\mathrm{int}$', 'CNT15a$_\\mathrm{int}$', 'CNT10a$_\\mathrm{int}$')
cmap_list = (0,0.2,0.35,0.5,0.65,0.8,0.99)
linestyle = ('-', '-', '-', '-', '-', '-', '-')
WaterO_upper_ylim = 0.004

cm = plt.cm.get_cmap('viridis')

functional_groups = ('DA', 'Amine', 'Ring', 'Quinone')#, 'Water', 'WaterO')

for j in range(len(functional_groups)):
    fig, ax = plt.subplots(figsize=(4,3))
    ax2 = ax.twinx()
    for i in range(len(systems)):
        filename = '/Users/jiaqz/Desktop/DA/' + systems[i] + \
            '/nvt/functional_groups_z_distn.txt'
        df = pd.read_csv(filename, delimiter = ' ', \
                         names = ['bins', 'DA', 'Amine', 'Ring', 'Quinone', \
                                  'Water', 'WaterO'], \
                         header = None)
        ax.plot(df['bins'], df[functional_groups[j]], linestyle=linestyle[i], \
                 c=cm(cmap_list[i]), label = legends[i])  
        # ax2.step(df['bins'], df['WaterO'], linestyle=':', c=cm(cmap_list[i]), \
        #         label='')
            
        # filename = '/Users/jiaqz/Desktop/DA/' + systems[i] + \
        #     '/nvt/water_z_distn.txt'
        # df = pd.read_csv(filename, delimiter = ' ', \
        #                  names = ['bins', 'Water', 'WaterO'], \
        #                  header = None)
        # if ('graphene' in systems[i]) or ('boronnitride' in systems[i]): 
        #     # Flat surfaces.
        #     ax2.step(df['bins'], df['WaterO'], linestyle=':', c=cm(cmap_list[i]))  
        # if ('ext' in systems[i]): # on the exterior.
        #     ax2.step(df['bins'], df['WaterO'], linestyle=':', c=cm(cmap_list[i]))  
        # elif ('int' in systems[i]): # reverse water velocity profiles if on the interior.
        #     ax2.step(-df['bins'], df['WaterO'], linestyle=':', c=cm(cmap_list[i]))  

    filename = '/Users/jiaqz/Desktop/DA/graphene/nvt/water_z_distn.txt'
    df = pd.read_csv(filename, delimiter = ' ', \
                     names = ['bins', 'Water', 'WaterO'], \
                     header = None)
    ax2.step(df['bins'], df['WaterO'], linestyle=':', color='r')  

    #ax2.plot(df['bins'], np.repeat(33,len(df['bins'])), '--r')
    ax2.set_ylim((0,120))
    #ax2.set_xlim((0,10))
    ax2.set_ylabel("$\\rho_N(\mathrm{water})$ (nm$^{-3}$)")
    ax.set_xlabel('Distance from the surface ($\\mathrm{\AA}$)')
    

    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width*0.85, box.height])

    ax.legend(legends, loc='center left', frameon=True, bbox_to_anchor=(1, 0.5))

    

    ax.set_ylabel("Probability, $p(d)$")
    #ax.set_ylim((0, 0.010))
    ax.set_xlim((2, 8))
    ax.set_xlabel("Distance to Surface, $d\ \\mathrm{(\\AA)}$")
    a,b = ax.get_ylim()
    WaterO_lower_ylim = a*WaterO_upper_ylim/b
    #ax2.set_ylim((WaterO_lower_ylim, WaterO_upper_ylim))
    ax2.set_ylabel("$\\rho(\\Delta z)_\mathrm{WaterO}$")
    ax2.yaxis.label.set_color([1,0,0,0.5])
    
    plt.savefig('/Users/jiaqz/Desktop/images/101_z_distn_armchair_' + functional_groups[j] + '.png', \
                dpi=300, bbox_inches='tight')
    plt.close('all')


from matplotlib.lines import Line2D
fig, ax = plt.subplots(figsize=(4,3))  
ax.legend([Line2D([0], [0], linestyle='-', color='k', lw=1), \
           Line2D([0], [0], linestyle=':', color='k', lw=1)], \
           ['Moieties', 'Water'], loc='center left', frameon=True, bbox_to_anchor=(1.24, 0.85))
plt.savefig('/Users/jiaqz/Desktop/images/101_legends.png', \
            dpi=300, bbox_inches='tight')
plt.close('all')

# import os
# os.system('convert /Users/jiaqz/Desktop/images/legends.png \
#            -crop +1242+0 -crop -0-523 /Users/jiaqz/Desktop/images/legends.png')
# os.system('convert /Users/jiaqz/Desktop/images/101_z_distn_armchair_DA.png \
#            -gravity northeast /Users/jiaqz/Desktop/images/legends.png \
#            -geometry +25+0 -composite /Users/jiaqz/Desktop/images/101_z_distn_armchair_DA.png')
# os.system('convert /Users/jiaqz/Desktop/images/101_z_distn_armchair_Quinone.png \
#            -gravity northeast /Users/jiaqz/Desktop/images/legends.png \
#            -geometry +25+0 -composite /Users/jiaqz/Desktop/images/101_z_distn_armchair_Quinone.png')
# os.system('convert /Users/jiaqz/Desktop/images/101_z_distn_armchair_Ring.png \
#            -gravity northeast /Users/jiaqz/Desktop/images/legends.png \
#            -geometry +25+0 -composite /Users/jiaqz/Desktop/images/101_z_distn_armchair_Ring.png')
# os.system('convert /Users/jiaqz/Desktop/images/101_z_distn_armchair_Amine.png \
#            -gravity northeast /Users/jiaqz/Desktop/images/legends.png \
#            -geometry +25+0 -composite /Users/jiaqz/Desktop/images/101_z_distn_armchair_Amine.png')
# os.system('rm /Users/jiaqz/Desktop/images/legends.png')
# 
# os.system('convert /Users/jiaqz/Desktop/images/101_z_distn_armchair_Quinone.png -crop -430-0 \
#            /Users/jiaqz/Desktop/images/101_z_distn_armchair_Quinone.png')
# os.system('convert /Users/jiaqz/Desktop/images/101_z_distn_armchair_Ring.png -crop -430-0 \
#            /Users/jiaqz/Desktop/images/101_z_distn_armchair_Ring.png')
# 