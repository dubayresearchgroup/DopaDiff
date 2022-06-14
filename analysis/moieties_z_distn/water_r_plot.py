######################################
# water_r_plot.py Revision 1.0 [07-21-2020]
#
# Changelog:
# V1.0 [07-21-2020]
# Initial commit.
######################################

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

filename = 'water_z_distn.txt'
df = pd.read_csv(filename, delimiter = ' ', \
                 names = ['bins', 'water', 'waterO'], \
                 header = None)

fig, ax = plt.subplots()
ax.plot(df['bins'], df['water'], 'b')
ax.plot(df['bins'], df['waterO'], 'r')
ax.plot(df['bins'], np.repeat(33, len(df['bins'])), '--k')
ax.set_ylim((-5,125))
ax.set_xlim((-10,10))
ax.set_xlabel('$\\Delta r/\\mathrm{\\AA}$')
ax.set_ylabel('$\\rho(\\Delta r)$')
ax.legend(['Water','WaterO'])
plt.savefig("water_r_distn.png", dpi=300, bbox_inches='tight')
plt.close("all")