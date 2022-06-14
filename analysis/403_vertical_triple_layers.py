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

systems = ('graphene','graphene3')
legends = ('Single\nLayer\nGraphene',\
           'Triple\nLayer\nGraphene')
linestyles = ('-', '--')
cm = plt.cm.get_cmap('viridis')

# =============================================================================
# 1. Differently curved carbon surfaces.
# =============================================================================

fig, ax = plt.subplots(figsize=(4,3))
filename = '/Users/jiaqz/Desktop/DA/graphene/nvt/functional_groups_z_distn.txt'
df = pd.read_csv(filename, delimiter = ' ', \
                 names = ['bins', 'COM', 'Amine', 'Ring', 'Quinone'], \
                 header = None)
ax.plot(df['bins'], df['COM'], '-k')
filename = '/Users/jiaqz/Desktop/DA/graphene3/nvt/functional_groups_z_distn.txt'
df = pd.read_csv(filename, delimiter = ' ', \
                 names = ['bins', 'COM', 'Amine', 'Ring', 'Quinone'], \
                 header = None)
ax.plot(df['bins'], df['COM'], '--k')

filename = '/Users/jiaqz/Desktop/DA/graphene/nvt/functional_groups_z_distn.txt'
df = pd.read_csv(filename, delimiter = ' ', \
                 names = ['bins', 'COM', 'Amine', 'Ring', 'Quinone'], \
                 header = None)
ax.plot(df['bins'], df['Amine'], '-b')
ax.plot(df['bins'], df['Ring'], '-', color='gray')
ax.plot(df['bins'], df['Quinone'], '-r')  

filename = '/Users/jiaqz/Desktop/DA/graphene3/nvt/functional_groups_z_distn.txt'
df = pd.read_csv(filename, delimiter = ' ', \
                 names = ['bins', 'COM', 'Amine', 'Ring', 'Quinone'], \
                 header = None)
ax.plot(df['bins'], df['Amine'], '--b')
ax.plot(df['bins'], df['Ring'], '--', color='gray')
ax.plot(df['bins'], df['Quinone'], '--r')  

ax.set_xlim((2,8)); ax.set_ylim((0,0.03))
ax.set_xlabel('Distance to Surface, $d (\\mathrm{\\AA})$')
ax.set_ylabel('Probability, $p(d)$')
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width*0.85, box.height])
ax.legend(legends, loc='center left', frameon=True, bbox_to_anchor=(1, 0.5))
plt.savefig('../images/403_vertical_triple_layers.png', \
            dpi=300, bbox_inches='tight')
plt.close("all")