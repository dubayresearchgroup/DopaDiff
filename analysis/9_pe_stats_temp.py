#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 12:00:46 2019

@author: qj3fe
"""

# Compute the MSDs and VACFs of graphene25 systems.
# =============================================================================
# 1. Traj
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('science')

systems = ('CNT10a_int', 'CNT15a_int', 'CNT20a_int', 'graphene',\
           'CNT20a_ext', 'CNT15a_ext', 'CNT10a_ext')
legends = ('CNT10a$_\\mathrm{int}$', 'CNT15a$_\\mathrm{int}$', 'CNT20a$_\\mathrm{int}$', 'Graphene',\
           'CNT20a$_\\mathrm{ext}$', 'CNT15a$_\\mathrm{ext}$', 'CNT10a$_\\mathrm{ext}$')
cm = plt.cm.get_cmap('viridis')
cmap_list = (0.99,0.8,0.65,0.5,0.35,0.2,0.0)

fig,axes = plt.subplots(1,7, sharey=True, \
                      gridspec_kw={'hspace': 0, 'wspace': 0}, figsize=(10,4))
bins = np.arange(0,5.00001,0.00001)
for j in range(len(systems)):
    filename = '/Users/jiaqz/Desktop/DA/' + systems[j] + '/nvt/0/data.out'
    pe = \
        np.genfromtxt(filename, skip_header=23, skip_footer=36, \
                      usecols=(28), unpack=True)
    axes[j].plot(bins, pe, c=cm(cmap_list[j]), lw=0.1)
axes[3].set_xlabel('Time (ns)')
axes[0].set_ylabel('PE (kcal/mol)')
#ax.legend(systems)

# box = ax.get_position()
# ax.set_position([box.x0, box.y0, box.width*0.85, box.height])

# axes[6].legend(legends, loc='center left', bbox_to_anchor=(1.02, 0.5))
# plt.tight_layout()

plt.savefig('/Users/jiaqz/Desktop/images/9_pe_traj_1.png', dpi=300, bbox_inches='tight')

# =============================================================================
# 
# =============================================================================
fig,ax = plt.subplots(figsize=(4,3))
bins = np.arange(-22.5, -2.5, 0.01)
for j in range(len(systems)):
    pe = np.zeros(0)
    for k in range(10):
        print(systems[j], k)
        filename = '/Users/jiaqz/Desktop/DA/' + systems[j] + '/nvt/' + str(k) + '/data.out'
        pe = np.append( pe, \
            np.genfromtxt(filename, skip_header=23, skip_footer=36, \
                          usecols=(28), unpack=True) )
    counts, _ = np.histogram(pe, bins=bins)        
    ax.step(bins[1:], counts/pe.size, c=cm(cmap_list[j]))
ax.set_xlabel('PE (kcal/mol)')
ax.set_ylabel('PE Distributions')
#ax.legend(systems)

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width*0.85, box.height])

ax.legend(legends, loc='center left', frameon=True, bbox_to_anchor=(1.02, 0.5))
plt.tight_layout()

plt.savefig('/Users/jiaqz/Desktop/images/9_pe_traj_2.png', dpi=300, bbox_inches='tight')