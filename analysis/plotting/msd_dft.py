######################################
# msd_dft.py Revision 1.0 [ 10-15-2020 ]
#
# Changelog:
# V1.0 [10-15-202]
# Compute vibrational freq along the direction perpendicular to the surface.
######################################

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
plt.style.use(['science', 'muted'])

# =============================================================================
# 1. Overall Plotting
# =============================================================================

surface = os.getcwd().split('/')[5].split('_')[0]

if surface == 'graphene' or surface == 'graphene3' or surface == 'groove':
    legend = 'z'
    filename = 'msd_vacf_10.out'
else:
    legend = 'r'
    filename = 'msd_vacf_10_raw.out'
    
df = pd.read_csv(filename, delimiter = ' ', \
                 names = ['bins', 'Dx', 'Dy', 'Dz', 'vacfx', 'vacfy', 'vacfz'], \
                 header = None)

signal = df['Dz']
fourier = np.fft.fft(signal)
n = signal.size
timestep = 0.01
freq = np.fft.fftfreq(n, d=timestep)
nfft = np.abs(fourier)
# freq[np.r_[True, nfft[1:] > nfft[:-1]] & np.r_[nfft[:-1] > nfft[1:], True]][1]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5,4)) 
plt.subplots_adjust(hspace = 0.3)
ax1.set_xlabel('Time (ps)')
ax1.set_ylabel("MSD$_" + legend + "$ ($\mathrm{\AA}^2$)")
ax1.plot(df['bins'], df['Dz'], '-b') 

ax2.plot(freq[0:n//2],nfft[0:n//2], '-r')
ax2.set_xlabel('Frequency (THz)')
ax2.set_ylabel('Amplitude') 
plt.savefig('1_1_msd_dft.png', dpi=300, bbox_inches='tight')

# =============================================================================
# 2. Statistics
# =============================================================================
adsorbate, surface = os.getcwd().split('/')[4:6]
ofilename = 'tex_stats.tex'
f = open(ofilename, 'a+')
header_string = '{}\t&\t{}\t&\t'
f.write(header_string.format(adsorbate, surface.replace('_', '\_')))

mass = {
    "DA" : 153.18,
    "DAH": 154.19,
    "DOQ": 151.16,
    "DOQH": 152.17,
    "Adatom": 153.18,
    "Ag": 107.87,
}

frequency = np.zeros(10)
force_constant = np.zeros(10)

for j in range(10):
    ifilename = str(j) + '/' + filename
    df = pd.read_csv(ifilename, delimiter = ' ', \
                     names = ['bins', 'Dx', 'Dy', 'Dz', 'vacfx', 'vacfy', 'vacfz'], \
                     header = None)
    signal = df['Dz']
    fourier = np.fft.fft(signal)
    n = signal.size
    timestep = 0.01
    freq = np.fft.fftfreq(n, d=timestep)
    nfft = np.abs(fourier)
    # Frequency unit THz.
    frequency[j] = freq[np.r_[True, nfft[1:] > nfft[:-1]] & np.r_[nfft[:-1] > nfft[1:], True]][1]
    # Force constant unit 1e13 N/\AA.
    force_constant[j] = frequency[j]*frequency[j]*mass[adsorbate]/100
        
stats_string = '${}\t\\pm\t{}$\t&\t${}\t\\pm\t{}$\t\\\\\n'
f.write(stats_string.format(np.around(frequency.mean(), 2),
                            np.around(frequency.std(), 2),
                            np.around(force_constant.mean(), 2),
                            np.around(force_constant.std(), 2),
                            )
        )
f.close()
print(frequency)
