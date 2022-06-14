######################################
# functional_groups_r_distn.py Revision 1.0 [07-19-2020]
#
# Changelog:
# V1.0 [07-19-2020]
# Initial commit.
######################################

# Generate r distributions of functional groups of DA on CNTs.

# =============================================================================
# 1. Overall COM distribution of DA.
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
import os
plt.style.use('science')

lx_line = 13
ly_line = 14

r = np.zeros(shape=(4,5000010))
labels = ['DA','Amine','Ring','Quinone']
color_list = ('k', 'b', 'gray', 'r')

surface = os.getcwd().split('/')[5].split('_')[0]
diameter_dict = {
    "CNT7a": 14.895,
    "CNT10a": 20.311,
    "CNT15a": 29.790,
    "CNT20a": 39.269,
    "CNT7z": 14.854,
    "CNT10z": 20.326,
    "CNT15z": 29.708,
    "CNT20z": 39.871,
}
radius = diameter_dict[surface]/2.
center_dict = {
    "CNT10a": 25,
    "CNT15a": 30,
    "CNT20a": 35,
    "CNT10z": 25,
    "CNT15z": 30,
    "CNT20z": 35, 
}
center = center_dict[surface]

data_file_header = 23
data_file_footer = 36
bins = np.arange(1,11,0.01)

for i in range(10):
    print(i)
    filename = str(i) + "/data.out"
    temp_x, temp_y, temp_amine_x, temp_amine_y, temp_ring_x, temp_ring_y, \
    temp_quinone_x, temp_quinone_y = \
        np.genfromtxt(filename, \
                      skip_header=data_file_header, \
                      skip_footer=data_file_footer, \
                      usecols=(1,2,7,8,10,11,13,14), \
                          unpack=True)

    with open(str(i) + '/after_nvt.data', "r") as f:
        for j, line in enumerate(f):
            if j == lx_line:
                lx = np.float(line.split(' ')[1]) - np.float(line.split(' ')[0])
            if j == ly_line:
                ly = np.float(line.split(' ')[1]) - np.float(line.split(' ')[0])

    # Wrap the simulation box.
    r[0,i*500001:(i+1)*500001] = np.abs( np.sqrt((temp_x%lx-center)**2 + \
                                                 (temp_y%ly-center)**2) - \
                                        radius)
    r[1,i*500001:(i+1)*500001] = np.abs( np.sqrt((temp_amine_x%lx-center)**2 + \
                                                 (temp_amine_y%ly-center)**2) - \
                                        radius)
    r[2,i*500001:(i+1)*500001] = np.abs( np.sqrt((temp_ring_x%lx-center)**2 + \
                                                 (temp_ring_y%ly-center)**2) - \
                                        radius)
    r[3,i*500001:(i+1)*500001] = np.abs( np.sqrt((temp_quinone_x%lx-center)**2 + \
                                                 (temp_quinone_y%ly-center)**2) - \
                                        radius)
    
   
fig, ax = plt.subplots(figsize=(5,4))
ofilename = 'functional_groups_r_stats.tex'
f = open(ofilename, 'a+')
stats_string = '\t{}\t&\t{}\t&\t{}\t&\t{}\t&\t{}\t\\\\\n'
for k in range(4):
    counts, _ = np.histogram(r[k], bins)
    new_counts = counts/(bins[1:]*(counts/bins[1:]).sum())
    ax.plot(bins[1:], new_counts, color=color_list[k])
    f.write(stats_string.format(labels[k], np.around(r[k].min(),3), np.around(r[k].max(), 3),\
                                np.around(r[k].mean(),3), np.around(bins[counts.argmax()],3)))
f.close()
ax.set_xlim((2,8)); ax.set_ylim((0,0.03))
ax.set_xlabel('Distance to Surface, $d (\\mathrm{\\AA})$')
ax.set_ylabel('Probability, $p(d)$')
ax.legend(labels, frameon=True)
plt.savefig("functional_groups_r_distn.png", dpi=300, bbox_inches='tight')
plt.close("all")


# =============================================================================
# file output.
# =============================================================================

counts0, _ = np.histogram(r[0], bins)
counts1, _ = np.histogram(r[1], bins)
counts2, _ = np.histogram(r[2], bins)
counts3, _ = np.histogram(r[3], bins)

np.savetxt('functional_groups_z_distn.txt', \
           np.c_[bins[1:], counts0/(bins[1:]*((counts0/bins[1:]).sum())), \
                 counts1/(bins[1:]*((counts1/bins[1:]).sum())), \
                 counts2/(bins[1:]*((counts2/bins[1:]).sum())), \
                 counts3/(bins[1:]*((counts3/bins[1:]).sum()))])