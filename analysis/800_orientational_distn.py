#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 14:34:25 2020

@author: qj3fe
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.style.use('science')

systems = ('CNT10a_ext', 'CNT15a_ext', 'CNT20a_ext', 'graphene',\
           'CNT20a_int', 'CNT15a_int', 'CNT10a_int')
legends = ('CNT10a$_\\mathrm{ext}$', 'CNT15a$_\\mathrm{ext}$', 'CNT20a$_\\mathrm{ext}$',  'Graphene',\
           'CNT20a$_\\mathrm{int}$', 'CNT15a$_\\mathrm{int}$', 'CNT10a$_\\mathrm{int}$')
cmap_list = (0,0.2,0.35,0.5,0.65,0.8,0.99)
cm = plt.cm.get_cmap('viridis')
linestyle = ('-', '-', '-', '-', '-', '-', '-')

fig,ax = plt.subplots(figsize=(4,3))
for j in range(len(systems)):
    filename = '../DA/' + systems[j] + '/nvt/orientational_distn.txt'
    df = pd.read_csv(filename, delimiter = ' ', \
                     names = ['bins', 'phi', 'theta'], \
                     header = None)
    ax.plot( (df['bins']/np.pi)*180, df['phi'], c=cm(cmap_list[j]))

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width*0.85, box.height])
ax.set_xlim((-25,25))
ax.set_xlabel("$\\phi$ ($^{\circ}$)")
ax.set_ylabel("Probability, $p(\\phi)$")
ax.legend(legends, frameon=True, bbox_to_anchor=(1.0, 0.8))
ylo, yhi = ax.get_ylim()[0], ax.get_ylim()[1]
ax.plot([0,0], [ylo, yhi], '--k')
ax.set_ylim((ylo,yhi))
#plt.savefig('../8_phi_distn.png', dpi=300, bbox_inches='tight')
plt.savefig('../images/8_phi_distn.png', dpi=300, bbox_inches='tight')
# =============================================================================
# 
# =============================================================================
"""
fig, axes = plt.subplots(7, sharex=True, sharey=True, gridspec_kw={'hspace': 0}, figsize=(4,3))
handles = []
for j in range(len(systems)):
    filename =  '../DA/' + systems[j] + '/nvt/orientational_distn.txt'
    df = pd.read_csv(filename, delimiter = ' ', \
                     names = ['bins', 'phi', 'theta'], \
                     header = None)
    # forward = np.asarray(df['theta'])
    # backward = np.asarray(df['theta'][::-1])
    # forward_shift = np.roll(df['theta'], len(df['bins'])//2)
    # backward_shift = np.roll(df['theta'][::-1], len(df['bins'])//2)
    # array = (forward + backward + forward_shift + backward_shift)/4.
    # ax.plot((df['bins']/np.pi)*180, array+0.002*j, c=cm(cmap_list[j]))
    handles += axes[j].step((df['bins'][::-1]/np.pi)*180, df['theta'], c=cm(cmap_list[j]), label=legends[j])
    axes[j].axes.yaxis.set_ticks([])

    box = axes[j].get_position()
    axes[j].set_position([box.x0, box.y0, box.width*0.85, box.height])
    axes[j].set_ylim((0,0.0025))
    axes[j].set_xlim((-180,180))
    
    # axes[j].legend(loc='center left', bbox_to_anchor=(1, 0.5))

ax = fig.add_subplot(111, frameon=False)
# hide tick and tick label of the big axis
ax.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
ax.set_xlabel("$\\theta$ (degrees)")
ax.set_ylabel("$\\theta$ distributions")

from matplotlib.legend import Legend
leg = Legend(ax, handles, legends,
             loc='center left', frameon=True, bbox_to_anchor=(0.85, 0.5))
ax.add_artist(leg);

# axes[6].set_xlabel('$\\theta$ (degrees)')
plt.tight_layout()
plt.savefig('../images/8_theta_distn.png', dpi=300)
"""

# =============================================================================
# Add symmetry.
# =============================================================================
fig, ax = plt.subplots(figsize=(4,3))
# handles = []
for j in range(len(systems)):
    filename =  '../DA/' + systems[j] + '/nvt/orientational_distn.txt'
    df = pd.read_csv(filename, delimiter = ' ', \
                     names = ['bins', 'phi', 'theta'], \
                     header = None)
    forward = np.asarray(df['theta'])
    backward = np.asarray(df['theta'][::-1])
    forward_shift = np.roll(df['theta'], len(df['bins'])//2)
    backward_shift = np.roll(df['theta'][::-1], len(df['bins'])//2)
    array = (forward + backward + forward_shift + backward_shift)/4.
    # handles += 
    ax.plot((df['bins']/np.pi)*180+90, array, c=cm(cmap_list[j]), label=legends[j])

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width*0.85, box.height])
ax.set_ylim((0,0.0015))
ax.set_xlim((0,90))
ax.set_xticks([0,30,60,90])
ax.set_yticks([0,0.0005,0.0010,0.0015])
    
ax.set_xlabel("$\\theta$ ($^{\circ}$)")
ax.set_ylabel("Probability, $p(\\theta)$")
ax.legend(legends, frameon=True, bbox_to_anchor=(1.02, 0.63))

# ax = fig.add_subplot(111, frameon=False)
# # hide tick and tick label of the big axis
# ax.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
# ax.set_xlabel("$\\theta$ ($^{\circ}$)")
# # ax.set_ylabel("$\\theta$ distributions")
# ax.text(-0.25,0.5, "$\\rho_\\theta$", fontsize=12, horizontalalignment='center',\
#         verticalalignment='center', rotation='vertical')
# 
# from matplotlib.legend import Legend
# leg = Legend(ax, handles, legends,
#              loc='center left', frameon=True, bbox_to_anchor=(0.85, 0.5))
# ax.add_artist(leg);

#plt.savefig('../8_theta_distn_symmetry.png', dpi=300, bbox_inches='tight')
plt.savefig('/Users/jiaqz/Desktop/images/8_theta_distn_symmetry.png', dpi=300, bbox_inches='tight')

import os 
os.system('convert /Users/jiaqz/Desktop/images/8_theta_distn_symmetry.png -crop +1025+191 /Users/jiaqz/Desktop/images/legends.png')
os.system('convert /Users/jiaqz/Desktop/images/8_theta_distn_symmetry.png -crop -379-0 \
           -gravity west -extent 1404x847 -gravity east /Users/jiaqz/Desktop/images/legends.png -composite\
           /Users/jiaqz/Desktop/images/8_theta_distn_symmetry.png')
os.system('rm /Users/jiaqz/Desktop/images/legends.png')

# =============================================================================
# 
# =============================================================================
"""
fig,ax = plt.subplots()
for j in range(len(systems)):
    filename =  '../DA/' + systems[j] + '/nvt/orientational_distn.txt'
    df = pd.read_csv(filename, delimiter = ' ', \
                     names = ['bins', 'phi', 'theta', 'theta_lever', 'theta_parallel'], \
                     header = None)
    ax.plot(df['bins'], df['theta_parallel']+0.002*j, c=cm(cmap_list[j]))
    ax.plot(df['bins'], np.repeat(0.002*j, len(df['bins'])), '--', c=cm(cmap_list[j]))
#ax.set_xlim((-np.pi/2,np.pi/2))
ylo = ax.get_ylim()[0]
yhi = ax.get_ylim()[1]
#ax.plot([0,0],[ylo,yhi], '--k')
ax.set_ylim((ylo,yhi))
ax.set_ylim((-0.0005,0.016))
ax.set_xlabel('$\\theta$ (radians)')
ax.legend(legends, loc="upper right")
plt.savefig('../images/8_theta_parallel_distn.png', dpi=300, bbox_inches='tight')

fig,ax = plt.subplots()
for j in range(len(systems)):
    filename =  '../DA/' + systems[j] + '/nvt/orientational_distn.txt'
    df = pd.read_csv(filename, delimiter = ' ', \
                     names = ['bins', 'phi', 'theta', 'theta_lever', 'theta_parallel'], \
                     header = None)
    ax.plot(df['bins'], df['theta_lever']+0.002*j, c=cm(cmap_list[j]))
    ax.plot(df['bins'], np.repeat(0.002*j, len(df['bins'])), '--', c=cm(cmap_list[j]))
#ax.set_xlim((-np.pi/2,np.pi/2))
ylo = ax.get_ylim()[0]
yhi = ax.get_ylim()[1]
#ax.plot([0,0],[ylo,yhi], '--k')
ax.set_ylim((ylo,yhi))
ax.set_ylim((-0.0005,0.016))
ax.set_xlabel('$\\theta$ (radians)')
ax.legend(legends, loc="upper right")
plt.savefig('../images/8_theta_lever_distn.png', dpi=300, bbox_inches='tight')

########################
# Overlaid
########################
fig,ax = plt.subplots()
for j in range(len(systems)):
    filename =  '../DA/' + systems[j] + '/nvt/orientational_distn.txt'
    df = pd.read_csv(filename, delimiter = ' ', \
                     names = ['bins', 'phi', 'theta', 'theta_lever', 'theta_parallel'], \
                     header = None)
    forward = np.asarray(df['theta_parallel'])
    backward = np.asarray(df['theta_parallel'][::-1])
    forward_shift = np.roll(df['theta_parallel'], len(df['bins'])//2)
    backward_shift = np.roll(df['theta_parallel'][::-1], len(df['bins'])//2)
    array = (forward + backward + forward_shift + backward_shift)/4.
    ax.plot(df['bins'], array+0.002*j, c=cm(cmap_list[j]))
    ax.plot(df['bins'], np.repeat(0.002*j, len(df['bins'])), '--', c=cm(cmap_list[j]))
#ax.set_xlim((-np.pi/2,np.pi/2))
ylo = ax.get_ylim()[0]
yhi = ax.get_ylim()[1]
#ax.plot([0,0],[ylo,yhi], '--k')
ax.set_ylim((ylo,yhi))
ax.set_ylim((-0.0005,0.016))
ax.set_xlabel('$\\theta$ (radians)')
ax.legend(legends, loc="upper right")
plt.savefig('../images/8_theta_parallel_shift.png', dpi=300, bbox_inches='tight')

fig,ax = plt.subplots()
for j in range(len(systems)):
    filename =  '../DA/' + systems[j] + '/nvt/orientational_distn.txt'
    df = pd.read_csv(filename, delimiter = ' ', \
                     names = ['bins', 'phi', 'theta', 'theta_lever', 'theta_parallel'], \
                     header = None)
    forward = np.asarray(df['theta_lever'])
    backward = np.asarray(df['theta_lever'][::-1])
    forward_shift = np.roll(df['theta_lever'], len(df['bins'])//2)
    backward_shift = np.roll(df['theta_lever'][::-1], len(df['bins'])//2)
    array = (forward + backward + forward_shift + backward_shift)/4.
    ax.plot(df['bins'], array+0.002*j, c=cm(cmap_list[j]))
    ax.plot(df['bins'], np.repeat(0.002*j, len(df['bins'])), '--', c=cm(cmap_list[j]))
#ax.set_xlim((-np.pi/2,np.pi/2))
ylo = ax.get_ylim()[0]
yhi = ax.get_ylim()[1]
#ax.plot([0,0],[ylo,yhi], '--k')
ax.set_ylim((ylo,yhi))
ax.set_ylim((-0.0005,0.016))
ax.set_xlabel('$\\theta$ (radians)')
ax.legend(legends, loc="upper right")
plt.savefig('../images/8_theta_lever_shift.png', dpi=300, bbox_inches='tight')
"""
