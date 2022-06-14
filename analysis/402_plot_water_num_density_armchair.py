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
plt.style.use('science')

# =============================================================================
# 0. Initialization
# =============================================================================

systems = ('CNT10a_ext', 'CNT15a_ext', 'CNT20a_ext', 'graphene',
           'CNT20a_int', 'CNT15a_int', 'CNT10a_int')
legends = ('CNT10a$_\\mathrm{ext}$', 'CNT15a$_\\mathrm{ext}$', 'CNT20a$_\\mathrm{ext}$', 'Graphene',
           'CNT20a$_\\mathrm{int}$', 'CNT15a$_\\mathrm{int}$', 'CNT10a$_\\mathrm{int}$')
cmap_list = (0, 0.2, 0.35, 0.5, 0.65, 0.8, 0.99)
linestyle = ('-', '-', '-', '-', '-', '-', '-')

cm = plt.cm.get_cmap('viridis')

# =============================================================================
# 1. Differently curved carbon surfaces.
# =============================================================================

functional_groups = ('Water', 'WaterO')

for j in range(len(functional_groups)):
    fig, ax = plt.subplots(figsize=(4, 3))
    for i in range(len(systems)):
        filename = '/Volumes/Backup/DopaDiff/DA/' + systems[i] + \
            '/nvt/water_z_distn.txt'
        df = pd.read_csv(filename, delimiter=' ',
                         names=['bins', 'Water', 'WaterO'],
                         header=None)
        if ('graphene' in systems[i]) or ('boronnitride' in systems[i]):
            # Flat surfaces.
            ax.plot(df['bins'], df[functional_groups[j]], linestyle=linestyle[i],
                    c=cm(cmap_list[i]), label=legends[i])
        if ('ext' in systems[i]):  # on the exterior.
            ax.plot(df['bins'], df[functional_groups[j]], linestyle=linestyle[i],
                    c=cm(cmap_list[i]), label=legends[i])
        # reverse water velocity profiles if on the interior.
        elif ('int' in systems[i]):
            ax.plot(-df['bins'], df[functional_groups[j]], linestyle=linestyle[i],
                    c=cm(cmap_list[i]), label=legends[i])
    ylo = ax.get_ylim()[0]
    yhi = ax.get_ylim()[1]
    ax.plot(df['bins'], np.repeat(33, len(df['bins'])), '--r')
    #ax.plot([0,0],[-5,120], '--k')
    ax.set_ylim((-5, 120))
    ax.set_xlim((2, 8))
    ax.set_ylabel("$\\rho_N$(water) (nm$^{-3}$)")
    ax.set_xlabel('$d$ ($\\mathrm{\AA}$)')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width*0.85, box.height])
    ax.legend(loc='center left', frameon=True, bbox_to_anchor=(1, 0.5))

    plt.savefig('../images/402_' + functional_groups[j] + '_num_density_armchair.png',
                dpi=300, bbox_inches='tight')
    plt.close('all')
