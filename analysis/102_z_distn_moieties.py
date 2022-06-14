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
import os
plt.style.use('science')

# =============================================================================
# 1. Different species on flat graphene.
# =============================================================================

systems = ('CNT10a_ext', 'CNT15a_ext', 'CNT20a_ext', 'graphene',
           'CNT20a_int', 'CNT15a_int', 'CNT10a_int')
legends = ('CNT10a$_\\mathrm{ext}$', 'CNT15a$_\\mathrm{ext}$', 'CNT20a$_\\mathrm{ext}$',  'Graphene',
           'CNT20a$_\\mathrm{int}$', 'CNT15a$_\\mathrm{int}$', 'CNT10a$_\\mathrm{int}$')
cmap_list = (0, 0.2, 0.35, 0.5, 0.65, 0.8, 0.99)
linestyle = ('-', '-', '-', '-', '-', '-', '-')
WaterO_upper_ylim = 0.004

cm = plt.cm.get_cmap('viridis')

functional_groups = ('DA', 'Amine', 'Ring', 'Quinone')  # , 'Water', 'WaterO')

for j in range(len(functional_groups)):
    fig, ax = plt.subplots(figsize=(3, 2))
    for i in range(len(systems)):
        filename = '../DA/' + systems[i] + \
            '/nvt/functional_groups_z_distn.txt'
        df = pd.read_csv(filename, delimiter=' ',
                         names=['bins', 'DA', 'Amine', 'Ring', 'Quinone',
                                'Water', 'WaterO'],
                         header=None)
        ax.plot(df['bins'], df[functional_groups[j]], linestyle=linestyle[i],
                c=cm(cmap_list[i]), label=systems[i])

    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width*0.85, box.height])

    ax.legend(legends, loc='center left', bbox_to_anchor=(1.02, 1))

    ax.set_ylim((-0.002, 0.035))
    # ax.set_ylabel("$\\rho(\\Delta z)$")

    fig.text(-.06, 0.5, 'Probability, $p(d)$',
             ha='center', va='center', rotation='vertical')
    fig.text(0.425, -0.04,
             'Distance to Surface, $d\\ \\mathrm{(\\AA)}$', ha='center', va='center')

    ax.legend(legends, loc='center left', frameon=True, bbox_to_anchor=(1, .5))
    #ax[0,0].set_ylim((-0.001, 0.034))
    ax.set_xlim((2, 8))

    ax.set_xticks([2, 4, 6, 8])
    # ax[0,0].set_yticks([0, 0.005, 0.010])

    plt.savefig('../images/102_z_distn_' + functional_groups[j] + '.png',
                dpi=300, bbox_inches='tight')
    plt.close('all')

os.system(
    'convert ../images/102_z_distn_DA.png -crop +810+0 ../images/102_legends.png')
for j in range(len(functional_groups)):
    os.system('convert ../images/102_z_distn_' + functional_groups[j] + '.png \
                -crop -375+0 ../images/102_z_distn_' + functional_groups[j] + '.png')
