#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 12:00:46 2019

@author: qj3fe
"""

# Plot the MSDs and the VACFs of DA on flat graphene.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from scipy import stats
from scipy.optimize import curve_fit
import sys

argv = np.int(sys.argv[1])

fitting_range = np.asarray((argv, 1000))*100

#adsorbate, surface = os.getcwd().split('/')[4:6]
ofilename = 'tex_stats.tex'
f = open(ofilename, 'a+')
#header_string = '{}\t&\t{}\t&\t{}\t&\t{}\t&\t'
#f.write(header_string.format(adsorbate, surface.replace('_', '\_'), 2, argv))
# =============================================================================
# 1. Linearly fitting the MSDs.
# =============================================================================
filename = 'msd_vacf_2000.out'
df = pd.read_csv(filename, delimiter = ' ', \
                 names = ['bins', 'Dx', 'Dy', 'Dz', 'vacfx', 'vacfy', 'vacfz'], \
                 header = None)
    
slope, intercept, r_value, _, __ = \
    stats.linregress(df['bins'][fitting_range[0]: fitting_range[1]], \
                     df['Dx'][fitting_range[0]: fitting_range[1]] + \
                     df['Dy'][fitting_range[0]: fitting_range[1]])
stats_string = '{}\t&\t{}\t&\t'
f.write(stats_string.format(np.around(slope*2.5, 3),
                            np.around(r_value**2,4)))

# =============================================================================
# 2. Stacked MSD curves.
# =============================================================================

fig = plt.figure()
ax = fig.gca()

ax.set_ylabel("MSD ($\mathrm{\AA}^2$)")
#ax.set_ylim((0, 15))
#ax.set_xlim((0, 10))
ax.set_xlabel("Time (ps)")

cmap = plt.cm.get_cmap('Blues')
ax.plot(df['bins'], df['Dx']+df['Dy'], color=cmap(0.5))
ax.plot(df['bins'][fitting_range[0]: fitting_range[1]], \
        (df['bins'][fitting_range[0]: fitting_range[1]])*slope+intercept, \
        color = 'k', linestyle = ':')
    
# =============================================================================
# 3. Exponentially fitting the MSDs.
# =============================================================================
slope, intercept, r_value, _, __ = \
    stats.linregress(np.log(df['bins'][fitting_range[0]: fitting_range[1]]), \
                     np.log(df['Dx'][fitting_range[0]: fitting_range[1]] + \
                            df['Dy'][fitting_range[0]: fitting_range[1]]))
        
def func(t, n, D, C):
    return 4*D*t**n + C
popt, pcov = curve_fit(func, df['bins'][fitting_range[0]: fitting_range[1]], \
                       df['Dx'][fitting_range[0]: fitting_range[1]] + \
                       df['Dy'][fitting_range[0]: fitting_range[1]], p0=(1, 1, 0))


stats_string = '{}\t&\t{}'
f.write(stats_string.format(np.around(popt[1]*10, 3), \
                            np.around(popt[0], 3)))

# =============================================================================
# 4. Exponentially fitted line.
# =============================================================================

ax.plot(df['bins'][fitting_range[0]: fitting_range[1]], \
        func(df['bins'][fitting_range[0]: fitting_range[1]], *popt), \
        color = 'r', linestyle = '--')
    
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width*0.85, box.height])

ax.legend(['MSD', 'Linear\nFit', 'Exponential\nFit'], loc='center left', bbox_to_anchor=(1, 0.5))

plt.savefig('1_exponential_fitting.png', dpi=300, bbox_inches='tight')

f.write('\\\\\n')
f.close()