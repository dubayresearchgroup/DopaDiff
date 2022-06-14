######################################
# functional_groups_z_distn.py Revision 1.0 [07-19-2020]
#
# Changelog:
# V1.0 [07-19-2020]
# Initial commit.
######################################

# Generate z distributions of functional groups of DA on flat pristine graphene.

# =============================================================================
# 1. Overall COM distribution of DA.
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('science')

lz_line = 15
electrode_z = 15+3.55

z = np.zeros(shape=(4,5000010))
labels = ['DA','Amine','Ring','Quinone']
color_list = ('k', 'b', 'gray', 'r')

data_file_header = 23
data_file_footer = 36
bins = np.arange(1,11,0.01)

for i in range(10):
    print(i)
    filename = str(i) + "/data.out"
    temp_z, temp_amine_z, temp_ring_z, temp_quinone_z = \
        np.genfromtxt(filename, \
                      skip_header=data_file_header, \
                      skip_footer=data_file_footer, \
                      usecols=(3,9,12,15), \
                          unpack=True)
            
    with open(str(i) + '/after_nvt.data', "r") as f:
        for j, line in enumerate(f):
            if j == lz_line:
                lz = np.float(line.split(' ')[1]) - np.float(line.split(' ')[0])

    # Wrap the simulation box.
    z[0,i*500001:(i+1)*500001] = np.abs((temp_z % lz) - electrode_z) - 3.55
    z[1,i*500001:(i+1)*500001] = np.abs((temp_amine_z % lz) - electrode_z) - 3.55
    z[2,i*500001:(i+1)*500001] = np.abs((temp_ring_z % lz) - electrode_z) - 3.55
    z[3,i*500001:(i+1)*500001] = np.abs((temp_quinone_z % lz) - electrode_z) - 3.55
    
fig, ax = plt.subplots(figsize=(5,4))
ofilename = 'functional_groups_z_stats.tex'
f = open(ofilename, 'w+')
stats_string = '\t{}\t&\t{}\t&\t{}\t&\t{}\t&\t{}\t\\\\\n'
for k in range(4):
    counts, _ = np.histogram(z[k], bins)
    ax.plot(bins[1:], counts/len(z[k]), color=color_list[k])
    f.write(stats_string.format(labels[k], np.around(z[k].min(),3), np.around(z[k].max(), 3),\
                                np.around(z[k].mean(),3), np.around(bins[counts.argmax()],3)))
f.close()
ax.set_xlim((2,8)); ax.set_ylim((0,0.03))
ax.set_xlabel('Distance to Surface, $d (\\mathrm{\\AA})$')
ax.set_ylabel('Probability, $p(d)$')
ax.legend(labels, frameon=True)
plt.savefig("functional_groups_z_distn.png", dpi=300, bbox_inches='tight')
plt.close("all")


# =============================================================================
# file output.
# =============================================================================

counts0, _ = np.histogram(z[0], bins)
counts1, _ = np.histogram(z[1], bins)
counts2, _ = np.histogram(z[2], bins)
counts3, _ = np.histogram(z[3], bins)

np.savetxt('functional_groups_z_distn.txt', \
           np.c_[bins[1:], counts0/len(z[0]), counts1/len(z[1]), \
                 counts2/len(z[2]), counts3/len(z[3])])