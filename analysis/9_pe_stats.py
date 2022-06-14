#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 12:00:46 2019

@author: qj3fe
"""

# Compute the MSDs and VACFs of graphene25 systems.

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('science')

systems = ('CNT10a_int', 'CNT15a_int', 'CNT20a_int', 'graphene',\
           'CNT20a_ext', 'CNT15a_ext', 'CNT10a_ext')
legends = ('CNT10a$_\\mathrm{int}$', 'CNT15a$_\\mathrm{int}$', 'CNT20a$_\\mathrm{int}$', 'Graphene',\
           'CNT20a$_\\mathrm{ext}$', 'CNT15a$_\\mathrm{ext}$', 'CNT10a$_\\mathrm{ext}$')
cm = plt.cm.get_cmap('viridis')
cmap_list = (0.99,0.8,0.65,0.5,0.35,0.2,0.0)

fig,ax = plt.subplots()
bins = np.arange(0,5.00001,0.00001)
for j in range(len(systems)):
    filename = '/Users/jiaqz/Desktop/DA/' + systems[j] + '/nvt/0/data.out'
    pe = \
        np.genfromtxt(filename, skip_header=23, skip_footer=36, \
                      usecols=(28), unpack=True)
    ax.plot(bins, pe, c=cm(cmap_list[j]))
ax.set_xlabel('Time (ns)')
ax.set_ylabel('PE (kcal/mol)')
ax.set_xticks([0,1,2,3,4,5])
#ax.legend(systems)

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width*0.85, box.height])

ax.legend(legends, loc='center left', frameon=True, bbox_to_anchor=(1.02, 0.5))

plt.savefig('/Users/jiaqz/Desktop/images/9_pe_traj_1.png', dpi=300, bbox_inches='tight')

fig,ax = plt.subplots()
bins = np.arange(0,5.00001,0.00001)
for j in range(len(systems)):
    filename = '/Users/jiaqz/Desktop/DA/' + systems[j] + '/nvt/0/data.out'
    pe = \
        np.genfromtxt(filename, skip_header=23, skip_footer=36, \
                      usecols=(28), unpack=True)
    ax.plot(bins, pe, c=cm(cmap_list[j]), lw=0.1)
ax.set_xlabel('Time (ns)')
ax.set_ylabel('PE (kcal/mol)')
ax.set_xticks([0,1,2,3,4,5])
#ax.legend(systems)

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width*0.85, box.height])

ax.legend(legends, loc='center left', frameon=True, bbox_to_anchor=(1.02, 0.5))

plt.savefig('/Users/jiaqz/Desktop/images/9_pe_traj_2.png', dpi=300, bbox_inches='tight')


import os
os.system("convert $HOME/Desktop/images/9_pe_traj_1.png -crop +880+0 $HOME/Desktop/images/9_pe_traj_1.png")
os.system("convert $HOME/Desktop/images/9_pe_traj_2.png -crop -390-0 $HOME/Desktop/images/9_pe_traj_2.png")
os.system("convert $HOME/Desktop/images/9_pe_traj_2.png $HOME/Desktop/images/9_pe_traj_1.png +smush 0 $HOME/Desktop/images/9_pe_traj.png")
os.system("rm -rf $HOME/Desktop/images/9_pe_traj_1.png $HOME/Desktop/images/9_pe_traj_2.png")

f = open('../images/9_pe_stats.tex', 'w+')
ostring = '\t{}\t&\t{}\t$\\pm$\t{}\t\\\\\n'
for j in range(len(systems)):
    filename = '/Users/jiaqz/Desktop/DA/' + systems[j] + '/nvt/0/data.out'
    pe = \
        np.genfromtxt(filename, skip_header=23, skip_footer=36, \
                      usecols=(28), unpack=True)
    f.write(ostring.format(systems[j].replace('_', '\_'), \
                           np.around(pe.mean(), 1), \
                           np.around(pe.std(), 1)))
f.close()