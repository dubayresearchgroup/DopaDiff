######################################
# exponentially_fitting.py Revision 1.0 [07-15-2020]
#
# Changelog:
# V1.0 [07-15-2020]
# Initial commit.
######################################

# Exponentially fitting the MSDs.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from scipy import stats
from scipy.optimize import curve_fit

fitting_range = (400,999)

adsorbate, surface = os.getcwd().split('/')[4:6]
ofilename = 'tex_stats.tex'
f = open(ofilename, 'a+')
header_string = '{}\t&\t{}\t&\t'
f.write(header_string.format(adsorbate, surface.replace('_', '\_')))
# =============================================================================
# 1. Linearly fitting the MSDs.
# =============================================================================
filename = 'msd_vacf.out'
df = pd.read_csv(filename, delimiter = ' ', \
                 names = ['bins', 'Dx', 'Dy', 'Dz', 'vacfx', 'vacfy', 'vacfz'], \
                 header = None)

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