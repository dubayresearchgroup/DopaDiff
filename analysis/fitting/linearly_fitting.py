######################################
# linearly_fitting.py Revision 1.1.1 [07-15-2020]
#
# Changelog:
# V1.1.1 [07-15-2020]
# Commented out MSD_5ps.
# V1.1 [07-15-2020]
# New feature. Added MSD_5ps.
# V1.0 [07-15-2020]
# Initial commit.
######################################

# Linearly fitting the MSDs.

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
slopes_x = np.zeros(10)
slopes_y = np.zeros(10)
slopes_z = np.zeros(10)

for j in range(10):
    filename = str(j) + '/msd_vacf_10.out'
    df = pd.read_csv(filename, delimiter = ' ', \
                     names = ['bins', 'Dx', 'Dy', 'Dz', 'vacfx', 'vacfy', 'vacfz'], \
                     header = None)
        
    slope, intercept, r_value, _, __ = \
        stats.linregress(df['bins'][fitting_range[0]: fitting_range[1]], \
                         df['Dx'][fitting_range[0]: fitting_range[1]])
    slopes_x[j] = slope

    slope, intercept, r_value, _, __ = \
        stats.linregress(df['bins'][fitting_range[0]: fitting_range[1]], \
                         df['Dy'][fitting_range[0]: fitting_range[1]])
    slopes_y[j] = slope

    slope, intercept, r_value, _, __ = \
        stats.linregress(df['bins'][fitting_range[0]: fitting_range[1]], \
                         df['Dz'][fitting_range[0]: fitting_range[1]])
    slopes_z[j] = slope

# filename = 'msd_vacf_10.out'
# df = pd.read_csv(filename, delimiter = ' ', \
#                  names = ['bins', 'Dx', 'Dy', 'Dz', 'vacfx', 'vacfy', 'vacfz'], \
#                  header = None)
#     
# slope, intercept, r_value, _, __ = \
#     stats.linregress(df['bins'][fitting_range[0]: fitting_range[1]], \
#                      df['Dx'][fitting_range[0]: fitting_range[1]] + \
#                      df['Dy'][fitting_range[0]: fitting_range[1]])

# stats_string = '${}\t\\pm\t{}$\t&\t{}\t&\t${}\t\\pm\t{}$\\\\\n'
# f.write(stats_string.format(np.around(slopes.mean()*2.5, 2),
#                             np.around(slopes.std()*2.5, 2),
#                             np.around(r_value**2,4),
#                             np.around(msd5.mean(), 1),
#                             np.around(msd5.std(), 1)
#                             )
#         )

stats_string = '${}\t\\pm\t{}$\t&\t${}\t\\pm\t{}$\t&\t${}\t\\pm\t{}$\t&\t\\\\\n'
f.write(stats_string.format(np.around(slopes_x.mean()*5, 2),
                            np.around(slopes_x.std()*5, 2),
                            np.around(slopes_y.mean()*5, 2),
                            np.around(slopes_y.std()*5, 2),
                            np.around(slopes_z.mean()*5, 2),
                            np.around(slopes_z.std()*5, 2),
                            )
        )

# =============================================================================
# 2. Stacked MSD curves.
# =============================================================================

fig = plt.figure()
ax = fig.gca()

ax.set_ylabel("MSD ($\mathrm{\AA}^2$)")
ax.set_ylim((0, 15))
ax.set_xlim((0, 10))
ax.set_xlabel("Time (ps)")

cmap = plt.cm.get_cmap('Blues')
ax.plot(df['bins'], df['Dx']+df['Dy'], color=cmap(0.5))
ax.plot(df['bins'][fitting_range[0]: fitting_range[1]], \
        (df['bins'][fitting_range[0]: fitting_range[1]])*slope+intercept, \
        color = 'k', linestyle = ':')
    
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width*0.85, box.height])

ax.legend(['MSD', 'Linear\nFit', 'Exponential\nFit'], loc='center left', bbox_to_anchor=(1, 0.5))

plt.savefig('1_1_linearly_fitting.png', dpi=300, bbox_inches='tight')

f.close()