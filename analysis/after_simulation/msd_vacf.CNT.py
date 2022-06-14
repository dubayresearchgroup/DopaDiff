######################################
# msd_vacf.CNT.py Revision 1.2 [10-11-2020]
#
# Changelog:
# V1.2  [10-11-2020]
# Save both cylindrical VACFs and raw VACFs.
# V1.0 [07-13-2020]
# Initial commit.
######################################

# Compute the MSDs and VACFs of CNT systems.

import numpy as np
import sys
import os

# header = 23
# footer = 36

header = int(sys.argv[2])
footer = int(sys.argv[3])

lx = ly = float(sys.argv[4])
lz = float(sys.argv[5])

surface = os.getcwd().split('/')[5].split('_')[0]

r_list = {
    "CNT10a": 10.1555,
    "CNT10z": 10.163,
    "CNT15a": 14.895,
    "CNT15z": 14.854,
    "CNT20a": 19.6345,
    "CNT20z": 19.9355,
}

electrode_list = {
    "CNT10a": 25,
    "CNT10z": 25,
    "CNT15a": 30,
    "CNT15z": 30,
    "CNT20a": 35,
    "CNT20z": 35,
}
ref_x = electrode_list[surface]
ref_y = electrode_list[surface]

seqlength = int(sys.argv[1])
print(seqlength)
seqnum = 500000 - seqlength

msd_x = np.zeros((seqlength))
msd_y = np.zeros((seqlength))
msd_z = np.zeros((seqlength))
vacf_x = np.zeros((seqlength))
vacf_y = np.zeros((seqlength))
vacf_z = np.zeros((seqlength))
vacf_temp_x = np.zeros((seqlength))
vacf_temp_y = np.zeros((seqlength))
vacf_temp_z = np.zeros((seqlength))


for j in range(10):
    print(j)
    filename = str(j) + "/data.out"
# =============================================================================
# All length units are in \AA.
#
# 1. Import data and size check.
# =============================================================================
    temp_x, temp_y, temp_z = \
        np.genfromtxt(filename, skip_header=header, skip_footer=footer,
                      usecols=(1, 2, 3), unpack=True)
    temp_vx, temp_vy, temp_vz = \
        np.genfromtxt(filename, skip_header=header, skip_footer=footer,
                      usecols=(4, 5, 6), unpack=True)

    # with open('../moltemplate_files/' + os.getcwd().split('/')[4] + '_' + os.getcwd().split('/')[5] + '.data', "r") as f:
    #     for i, line in enumerate(f):
    #         if i == lx_line:
    #             lx = float(line.split(' ')[1]) - \
    #                 float(line.split(' ')[0])
    #         if i == ly_line:
    #             ly = float(line.split(' ')[1]) - \
    #                 float(line.split(' ')[0])
    #         if i == lz_line:
    #             lz = float(line.split(' ')[1]) - \
    #                 float(line.split(' ')[0])

    wrapped_x = temp_x % lx
    wrapped_y = temp_y % ly

# =============================================================================
# 2. Pre-processing and \theta continuation check.
# =============================================================================

    cutoff = np.pi/2
    theta = np.arctan2((wrapped_y - ref_y), (wrapped_x - ref_x))

    for i in range(1, theta.size):
        if np.abs(theta[i] - theta[i-1]) > cutoff:
            if theta[i] - theta[i-1] > 0:
                theta[i:] = theta[i:] - 2*np.pi
            else:
                theta[i:] = theta[i:] + 2*np.pi
    # theta = theta - theta[0]
# =============================================================================
# 3. Slicing the data string.
# =============================================================================
    # Compute the relative displacement against the top carbon surface.
    z = np.sqrt((wrapped_y - ref_y)**2 + (wrapped_x - ref_x)**2)
    x = z.mean()*theta
    y = temp_z

    vx = temp_vx*np.sin(theta)-temp_vy*np.cos(theta)
    vy = temp_vz
    vz = temp_vx*np.cos(theta)+temp_vy*np.sin(theta)

    seq_x = np.zeros(seqlength)
    seq_y = np.zeros(seqlength)
    seq_z = np.zeros(seqlength)

    seq_vx = np.zeros(seqlength)
    seq_vy = np.zeros(seqlength)
    seq_vz = np.zeros(seqlength)

    seq_temp_vx = np.zeros(seqlength)
    seq_temp_vy = np.zeros(seqlength)
    seq_temp_vz = np.zeros(seqlength)

    for i in range(seqnum):
        start_index = i
        end_index = i + seqlength

        # MSD
        seq_x = seq_x + (x[start_index:end_index] - x[start_index])**2
        seq_y = seq_y + (y[start_index:end_index] - y[start_index])**2
        seq_z = seq_z + (z[start_index:end_index] - z[start_index])**2

        # cylindrical VACFs
        seq_vx = seq_vx + (vx[start_index:end_index]) * (vx[start_index])
        seq_vy = seq_vy + (vy[start_index:end_index]) * (vy[start_index])
        seq_vz = seq_vz + (vz[start_index:end_index]) * (vz[start_index])
        # raw VACFs
        seq_temp_vx = seq_temp_vx + \
            (temp_vx[start_index:end_index]) * (temp_vx[start_index])
        seq_temp_vy = seq_temp_vy + \
            (temp_vy[start_index:end_index]) * (temp_vy[start_index])
        seq_temp_vz = seq_temp_vz + \
            (temp_vz[start_index:end_index]) * (temp_vz[start_index])

    msd_x = msd_x + seq_x/float(seqnum)
    msd_y = msd_y + seq_y/float(seqnum)
    msd_z = msd_z + seq_z/float(seqnum)
    vacf_x = vacf_x + seq_vx/float(seqnum)
    vacf_y = vacf_y + seq_vy/float(seqnum)
    vacf_z = vacf_z + seq_vz/float(seqnum)
    vacf_temp_x = vacf_temp_x + seq_temp_vx/float(seqnum)
    vacf_temp_y = vacf_temp_y + seq_temp_vy/float(seqnum)
    vacf_temp_z = vacf_temp_z + seq_temp_vz/float(seqnum)

    np.savetxt(str(j) + '/msd_vacf_' + str(seqlength//100) + '.out',
               np.c_[np.arange(0, seqlength)/100.0, seq_x/float(seqnum),
                     seq_y/float(seqnum), seq_z/float(seqnum),
                     seq_vx*10**6/float(seqnum), seq_vy *
                     10**6/float(seqnum),
                     seq_vz*10**6/float(seqnum)])
    np.savetxt(str(j) + '/msd_vacf_' + str(seqlength//100) + '_raw.out',
               np.c_[np.arange(0, seqlength)/100.0, seq_x/float(seqnum),
                     seq_y/float(seqnum), seq_z/float(seqnum),
                     seq_temp_vx*10**6 /
                     float(seqnum), seq_temp_vy*10**6/float(seqnum),
                     seq_temp_vz*10**6/float(seqnum)])

msd_x = msd_x/10.0
msd_y = msd_y/10.0
msd_z = msd_z/10.0
vacf_x = vacf_x/10.0
vacf_y = vacf_y/10.0
vacf_z = vacf_z/10.0
vacf_temp_x = vacf_temp_x/10.0
vacf_temp_y = vacf_temp_y/10.0
vacf_temp_z = vacf_temp_z/10.0

np.savetxt('msd_vacf_' + str(seqlength//100) + '.out',
           np.c_[np.arange(0, seqlength)/100.0, msd_x, msd_y, msd_z,
                 vacf_x*10**6, vacf_y*10**6, vacf_z*10**6])
np.savetxt('msd_vacf_' + str(seqlength//100) + '_raw.out',
           np.c_[np.arange(0, seqlength)/100.0, msd_x, msd_y, msd_z,
                 vacf_temp_x*10**6, vacf_temp_y*10**6, vacf_temp_z*10**6])
