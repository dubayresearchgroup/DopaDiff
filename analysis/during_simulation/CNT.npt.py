######################################
# CNT.npt.py Revision 1.0.2 [07-13-2020]
#
# Changelog:
# V1.0.2 [07-13-2020]
# Bug fix. "headers" now supports for DA derivatives.
# V1.0.1 [07-12-2020]
# Bug fix. Added "headers" dict for different surfaces.
######################################

# =============================================================================
# Finding the configurations in an NPT trajectory, whose volume is closest to
# the mean value.
# =============================================================================

import shutil 
import numpy as np
import copy
import matplotlib.pyplot as plt
import os

# =============================================================================
# Returns the index of the value is closest to the mean.
# =============================================================================
def find_nearest(array, value):
    idx = (np.abs(array - value)).argmin()
    return idx

path = ''
file_name = 'log.lammps'

surface = os.getcwd().split('/')[5].split('_')[0]
adsorbate = os.getcwd().split('/')[4]
if adsorbate != 'DA':
    surface = adsorbate

r_length = {
    "CNT10a": 50,
    "CNT15a": 60,
    "CNT20a": 70,
    "CNT10z": 50,
    "CNT15z": 60,
    "CNT20z": 70, 
    "Ag"    : 50, 
    "Adatom": 50,
    "DAH"   : 50,
    "DOQ"   : 50,
    "DOQH"  : 50,
}



headers = {
    "CNT10a": 562,
    "CNT15a": 562,
    "CNT20a": 562,
    "CNT10z": 569,
    "CNT15z": 569,
    "CNT20z": 569,
    "Ag"    : 525, 
    "Adatom": 525,
    "DAH"   : 572,
    "DOQ"   : 565,
    "DOQH"  : 567,
}
header = headers[surface]
column_number = (0,4)
footer = 27
num_of_means = 10

vol = np.genfromtxt(file_name, skip_header=header, skip_footer=footer,
                    usecols=(column_number))

mean = np.mean(vol[:,1])

MAX = 1000
tmpvol = copy.deepcopy(vol[:,1])
# ofilename = 'box_sizes.txt'
# f = open(ofilename, 'a+')
for i in range(num_of_means):
    index = find_nearest(tmpvol[:], mean)
    filename = 'restarts/restart.' + str(int(vol[index,0])) + '.dopa'
    destination = '../nvt/restart.' + str(int(vol[index,0])) + '.dopa'
    shutil.copyfile(filename, destination)
#     f.write('{}\t'.format(tmpvol[index]))
    tmpvol[index] = MAX
# f.close()

plt.scatter(vol[:,0]/1000000., vol[:,1], s=5, c='black', linewidths=0)
plt.title("$z$-Dimention in $NPT$ Equilibration")
plt.ylabel("Side Length / $\mathrm{\AA}$")
plt.xlabel("Time / ns")
plt.axvspan(0.25, 1, alpha=0.1, color='k')
plt.xlim([0,1])
plt.ylim([r_length[surface]-5,r_length[surface]+5])
plt.savefig('npt.png', dpi=300)
plt.close()