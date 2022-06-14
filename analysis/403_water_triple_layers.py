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
cm = plt.cm.get_cmap('viridis')

# =============================================================================
# 1. Differently curved carbon surfaces.
# =============================================================================

fig, ax = plt.subplots(figsize=(4,3))
filename = '/Users/jiaqz/Desktop/DA/graphene/nvt/water_z_distn.txt'
df = pd.read_csv(filename, delimiter = ' ', \
                 names = ['bins', 'Water', 'WaterO'], \
                 header = None)
ax.plot(df['bins'], df['WaterO'], '-', c=cm(0.5))  

filename = '/Users/jiaqz/Desktop/DA/graphene3/nvt/water_z_distn.txt'
df = pd.read_csv(filename, delimiter = ' ', \
                 names = ['bins', 'Water', 'WaterO'], \
                 header = None)
ax.plot(df['bins']-3.55, df['WaterO'], '-m')  

ylo=ax.get_ylim()[0]; yhi=ax.get_ylim()[1];  
ax.plot(df['bins'], np.repeat(33,len(df['bins'])), '--r')
#ax.plot([0,0],[-5,120], '--k')
ax.set_ylim((-5,120))
ax.set_xlim((2,8))
ax.set_ylabel("$\\rho_N$(water) (nm$^{-3}$)")
ax.set_xlabel('$d$ ($\\mathrm{\AA}$)')

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width*0.85, box.height])
ax.legend(legends, loc='center left', frameon=True, bbox_to_anchor=(1, 0.5))

plt.savefig('../images/403_water_triple_layers.png', \
            dpi=300, bbox_inches='tight')
plt.close('all')