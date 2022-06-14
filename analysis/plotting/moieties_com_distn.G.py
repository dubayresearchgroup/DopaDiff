######################################
# com_distn_plots.G.py Revision 1.0.1 [07-15-2020]
#
# Changelog:
# V1.0.1 [07-15-2020]
# Bug fix. Standardize the colorbar ranges.
######################################

# Generate COM distribution on flat pristine graphene.

import numpy as np

x_single = 1.418 * 2 * np.sqrt(3)
y_single = 1.418 * 6
amine_x = np.zeros((10, 500001))
amine_y = np.zeros((10, 500001))
ring_x = np.zeros((10, 500001))
ring_y = np.zeros((10, 500001))
quinone_x = np.zeros((10, 500001))
quinone_y = np.zeros((10, 500001))

header = 23
footer = 36

for j in range(10):
    print(j)
    filename = str(j) + "/data.out"
    temp_amine_x, temp_amine_y, temp_ring_x, temp_ring_y, \
    temp_quinone_x, temp_quinone_y = np.genfromtxt(filename, skip_header=header, skip_footer=footer,
                     usecols=(7,8,10,11,13,14), unpack=True)
    # Wrap the simulation box.
    amine_x[j] = temp_amine_x % x_single
    amine_y[j] = temp_amine_y % y_single
    ring_x[j] = temp_ring_x % x_single
    ring_y[j] = temp_ring_y % y_single
    quinone_x[j] = temp_quinone_x % x_single
    quinone_y[j] = temp_quinone_y % y_single

import matplotlib.pyplot as plt
plt.style.use('science')

for k, item in enumerate(['amine','ring','quinone']):

    if k == 0:
        x = amine_x; y = amine_y;
    elif k == 1:
        x = ring_x; y = ring_y;
    else:
        x = quinone_x; y = quinone_y;

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

    plt.savefig('3_' + item + '_com_distn.png', dpi=300, bbox_inches='tight')
    plt.close("all")