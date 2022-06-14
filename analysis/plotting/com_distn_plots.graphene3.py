######################################
# com_distn_plots.G.py Revision 1.2 [09-14-2020]
#
# Changelog:
# V1.2      [09-14-2020]
# Added SciencePlots style.
# Specified axes ticks.
# V1.1      [08-23-2020]
# Increase font size by specify figsize.
# V1.0.1 [07-15-2020]
# Bug fix. Standardize the colorbar ranges.
######################################

# Generate COM distribution on flat pristine graphene.

import numpy as np

x_single = 1.418 * 2 * np.sqrt(3)
y_single = 1.418 * 6
x = np.zeros((10, 500001))
y = np.zeros((10, 500001))

header = 23
footer = 36

for j in range(10):
    print(j)
    filename = str(j) + "/data.out"
    temp_x, temp_y = np.genfromtxt(filename, skip_header=header, skip_footer=footer,
                     usecols=(1,2), unpack=True)
    # Wrap the simulation box.
    x[j] = temp_x % x_single
    y[j] = temp_y % y_single

import matplotlib.pyplot as plt
plt.style.use('science')

fig, ax = plt.subplots(figsize=(2,3))
cm = plt.cm.get_cmap('Blues')
plt.axis('tight')
plt.axes().set_aspect('equal')
plt.axis([0, x_single, 0, y_single], 'scaled')
plt.xlim(0, x_single)
plt.ylim(0, y_single)
plt.ylabel('$y$/$\mathrm{\AA}$')
plt.xlabel('$x$/$\mathrm{\AA}$')
hist = plt.hist2d(x.flatten(), y.flatten(),
                  bins=(int(50*x_single),int(50*y_single)), cmap=cm)
cbar = plt.colorbar()
plt.clim(0,150)
cbar.set_ticks([0,50,100,150])
cbar.ax.set_title('Counts\n Per Pixel')
#cbar.ax.set_yticklabels(['Low\nDensity', 'High\nDensity'])

plt.xticks([0,2,4])
plt.yticks([0,2,4,6,8])

for i in [0,3,6]:
    for j in range(3):
        circle = plt.Circle((x_single/2*j, y_single/6*i), radius=0.5, fill=False,
                             edgecolor='grey', linestyle='--', linewidth=1)
        plt.gca().add_patch(circle)
for i in [2,5]:
    for j in range(3):
        circle = plt.Circle((x_single/2*j, y_single/6*i), radius=0.5, fill=False,
                             edgecolor='grey', linestyle='--', linewidth=1)
        plt.gca().add_patch(circle)
for i in [0.5,3.5]:
    for j in [0.5,1.5]:
        circle = plt.Circle((x_single/2*j, y_single/6*i), radius=0.5, fill=False,
                             edgecolor='grey', linestyle='--', linewidth=1)
        plt.gca().add_patch(circle)
for i in [1.5,4.5]:
    for j in [0.5,1.5]:
        circle = plt.Circle((x_single/2*j, y_single/6*i), radius=0.5, fill=False,
                             edgecolor='grey', linestyle='--', linewidth=1)
        plt.gca().add_patch(circle)

plt.plot([x_single/2, x_single/2], [0, y_single], 'k--')
plt.plot([0, x_single], [y_single/2, y_single/2], 'k--')

temp_x = np.array([0,1/4,1/2,3/4,1])
temp_y = np.array([0,1/12,0,1/12,0])
plt.plot(temp_x*x_single, temp_y*y_single, 'k-.', lw=1)

temp_x = np.array([0,1/4,1/2,3/4,1])
temp_y = np.array([1/3,1/4,1/3,1/4,1/3])
plt.plot(temp_x*x_single, temp_y*y_single, 'k-.', lw=1)

temp_x = np.array([0,1/4,1/2,3/4,1])
temp_y = np.array([1/2,7/12,1/2,7/12,1/2])
plt.plot(temp_x*x_single, temp_y*y_single, 'k-.', lw=1)

temp_x = np.array([0,1/4,1/2,3/4,1])
temp_y = np.array([5/6,3/4,5/6,3/4,5/6])
plt.plot(temp_x*x_single, temp_y*y_single, 'k-.', lw=1)

temp_x = np.array([1/4,1/4,1/2,1/2,1/4,1/4])
temp_y = np.array([1/12,1/4,1/3,1/2,7/12,3/4])
plt.plot(temp_x*x_single, temp_y*y_single, 'k-.', lw=1)

temp_x = np.array([3/4,3/4,1/2,1/2,3/4,3/4])
temp_y = np.array([1/12,1/4,1/3,1/2,7/12,3/4])
plt.plot(temp_x*x_single, temp_y*y_single, 'k-.', lw=1)

plt.tight_layout()
plt.savefig("3_com_distn_plot.png", dpi=300)
plt.close("all")