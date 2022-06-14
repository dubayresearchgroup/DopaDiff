#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 14:34:25 2020

@author: qj3fe
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.style.use('science')

adsorbates = ('DA', 'DAH', 'DOQ', 'DOQH')
legends = ('DA', 'DAH$^+$', 'DOQ', 'DOQH$^+$')
systems = ('graphene')
cm = plt.cm.get_cmap('viridis')
cmap_list = (0,0.3,0.6,0.99)

fig,ax = plt.subplots(figsize=(4,3))
for j in range(len(adsorbates)):
    print(j)
    filename = '../' + adsorbates[j] + '/graphene/nvt/orientational_distn.txt'
    df = pd.read_csv(filename, delimiter = ' ', \
                     names = ['bins', 'phi', 'theta'], \
                     header = None)
    if adsorbates[j] == 'DAH':
        ax.plot( (-df['bins']/np.pi)*180, df['phi'], c=cm(cmap_list[j]))
    else:
        ax.plot( (df['bins']/np.pi)*180, df['phi'], c=cm(cmap_list[j]))

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width*0.85, box.height])
ax.set_xlim((-25,25))
ax.set_xlabel("$\\phi$ ($^{\circ}$)")
ax.set_ylabel("Probability, $p(\\phi)$")
ax.legend(legends, frameon=True, bbox_to_anchor=(1.0, 0.7))
ylo, yhi = ax.get_ylim()[0], ax.get_ylim()[1]
ax.plot([0,0], [ylo, yhi], '--k')
ax.set_ylim((ylo,yhi))

#plt.savefig('../8_1_phi_distn.png', dpi=300, bbox_inches='tight')
plt.savefig('../images/8_1_phi_distn.png', dpi=300, bbox_inches='tight')
plt.close('all')

fig,ax = plt.subplots(figsize=(4,3))
for j in range(len(adsorbates)):
    print(j+10)
    filename = '../' + adsorbates[j] + '/graphene/nvt/orientational_distn.txt'
    df = pd.read_csv(filename, delimiter = ' ', \
                     names = ['bins', 'phi', 'theta'], \
                     header = None)

    forward = np.asarray(df['theta'])
    backward = np.asarray(df['theta'][::-1])
    forward_shift = np.roll(df['theta'], len(df['bins'])//2)
    backward_shift = np.roll(df['theta'][::-1], len(df['bins'])//2)
    array = (forward + backward + forward_shift + backward_shift)/4.
    ax.plot((df['bins']/np.pi)*180+90, array, c=cm(cmap_list[j]), label=legends[j])

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width*0.85, box.height])
ax.set_ylim((0,0.0015))
ax.set_xlim((0,90))
ax.set_xticks([0,30,60,90])
ax.set_yticks([0,0.0005,0.0010,0.0015])

ax.set_xlabel("$\\theta$ ($^{\circ}$)")
ax.set_ylabel("Probability, $p(\\theta)$")
ax.legend(legends, frameon=True, bbox_to_anchor=(1.01, 0.66))

#plt.savefig('../8_1_theta_distn.png', dpi=300, bbox_inches='tight')
plt.savefig('../images/8_1_theta_distn.png', dpi=300, bbox_inches='tight')
plt.close('all')