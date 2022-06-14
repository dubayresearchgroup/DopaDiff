######################################
# msd_vacf.G.py Revision 1.0 [07-13-2020]
#
# Changelog:
# V1.0 [07-13-2020]
# Initial commit.
######################################

# Compute the MSDs and VACFs of graphene systems.

import numpy as np
import sys

x_size = 98.2419
y_size = 97.8420

header = 23
footer = 36

seqlength = int(sys.argv[1])
print(seqlength)
seqnum = 500000 - seqlength

msd_x = np.zeros((seqlength))
msd_y = np.zeros((seqlength))
msd_z = np.zeros((seqlength))
vacf_x = np.zeros((seqlength))
vacf_y = np.zeros((seqlength))
vacf_z = np.zeros((seqlength))

for j in range(10):
    print(j)
    filename = str(j) + "/data.out"
    x, y, z = \
        np.genfromtxt(filename, skip_header=header, skip_footer=footer,
                      usecols=(1, 2, 3), unpack=True)
    vx, vy, vz = \
        np.genfromtxt(filename, skip_header=header, skip_footer=footer,
                      usecols=(4, 5, 6), unpack=True)

    seq_x = np.zeros(seqlength)
    seq_y = np.zeros(seqlength)
    seq_z = np.zeros(seqlength)

    seq_vx = np.zeros(seqlength)
    seq_vy = np.zeros(seqlength)
    seq_vz = np.zeros(seqlength)

    for i in range(seqnum):
        start_index = i
        end_index = i + seqlength

        # MSD
        seq_x = seq_x + (x[start_index:end_index] - x[start_index])**2
        seq_y = seq_y + (y[start_index:end_index] - y[start_index])**2
        seq_z = seq_z + (z[start_index:end_index] - z[start_index])**2

        # VACF
        seq_vx = seq_vx + (vx[start_index:end_index]) * (vx[start_index])
        seq_vy = seq_vy + (vy[start_index:end_index]) * (vy[start_index])
        seq_vz = seq_vz + (vz[start_index:end_index]) * (vz[start_index])

    np.savetxt(str(j) + '/msd_vacf_' + str(seqlength//100) + '.out',
               np.c_[np.arange(0, seqlength)/100.0, seq_x/np.float(seqnum),
                     seq_y/np.float(seqnum), seq_z/np.float(seqnum),
                     seq_vx*10**6/np.float(seqnum), seq_vy *
                     10**6/np.float(seqnum),
                     seq_vz*10**6/np.float(seqnum)])
    np.savetxt(str(j) + '/msd_vacf_' + str(seqlength//100) + '_raw.out',
               np.c_[np.arange(0, seqlength)/100.0, seq_x/np.float(seqnum),
                     seq_y/np.float(seqnum), seq_z/np.float(seqnum),
                     seq_vx*10**6/np.float(seqnum), seq_vy *
                     10**6/np.float(seqnum),
                     seq_vz*10**6/np.float(seqnum)])

    msd_x += seq_x/np.float(seqnum)
    msd_y += seq_y/np.float(seqnum)
    msd_z += seq_z/np.float(seqnum)
    vacf_x += seq_vx/np.float(seqnum)
    vacf_y += seq_vy/np.float(seqnum)
    vacf_z += seq_vz/np.float(seqnum)

msd_x = msd_x/10.0
msd_y = msd_y/10.0
msd_z = msd_z/10.0
vacf_x = vacf_x/10.0
vacf_y = vacf_y/10.0
vacf_z = vacf_z/10.0

np.savetxt('msd_vacf_' + str(seqlength//100) + '.out',
           np.c_[np.arange(0, seqlength)/100.0, msd_x, msd_y, msd_z,
                 vacf_x*10**6, vacf_y*10**6, vacf_z*10**6])
np.savetxt('msd_vacf_' + str(seqlength//100) + '_raw.out',
           np.c_[np.arange(0, seqlength)/100.0, msd_x, msd_y, msd_z,
                 vacf_x*10**6, vacf_y*10**6, vacf_z*10**6])
