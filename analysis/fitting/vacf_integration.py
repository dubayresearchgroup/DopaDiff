######################################
# vacf_integration.py Revision 1.0.0 [07-15-2020]
#
# Changelog:
# V1.0 [07-15-2020]
# Initial commit.
######################################

# Compute diffusion coefficients from Green-Kubo relation.

import numpy as np
import pandas as pd
import os

fitting_range = (0,999)

adsorbate, surface = os.getcwd().split('/')[4:6]
ofilename = 'tex_stats.tex'
f = open(ofilename, 'a+')
header_string = '{}\t&\t{}\t&\t'
f.write(header_string.format(adsorbate, surface.replace('_', '\_')))
# =============================================================================
# 1. D from the Green-Kubo relation.
# =============================================================================

D = np.zeros(10)
for j in range(10):
    filename = str(j) + '/msd_vacf_10.out'
    df = pd.read_csv(filename, delimiter = ' ', \
                     names = ['bins', 'Dx', 'Dy', 'Dz', 'vacfx', 'vacfy', 'vacfz'], \
                     header = None)
        
    Dx = df['vacfx'].sum()/100.
    Dy = df['vacfy'].sum()/100.
    Dz = df['vacfz'].sum()/100.
    D[j] = (Dx+Dy)/2.


stats_string = '${}\t\\pm\t{}$\t\\\\\n'
f.write(stats_string.format(np.around(D.mean()*10, 2), np.around(D.std()*10, 2)))
f.close()
