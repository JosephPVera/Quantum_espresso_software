import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('silicon_bands.dat.gnu')

k = np.unique(data[:, 0])
bands1 = np.reshape(data[:, 1], (-1, len(k)))

VBM = 6.2107

# Rescale energy with respect to the VBM
bands = bands1 - VBM

for band in range(len(bands)):
    plt.plot(k, bands[band, :], linewidth=1, color='xkcd:blue')
plt.xlim(min(k), max(k))
 
# VBM = 6.2107 eV and CBM = 6.7835 eV
Gap = 0.5728
plt.axhline(0, linestyle='--', linewidth=0.75, color='xkcd:black')
plt.axhline(Gap, linestyle='--', linewidth=0.75, color='xkcd:black')

# High symmetry k-points 
plt.axvline(0.866025, linewidth=0.2, color='xkcd:black')
plt.axvline(1.866025, linewidth=0.2, color='xkcd:black')
plt.axvline(2.219579, linewidth=0.2, color='xkcd:black')
plt.axvline(3.280239, linewidth=0.2, color='xkcd:black')

# High symmetry points
plt.xticks(ticks= [0, 0.866025, 1.866025, 2.219579, 3.280239], labels=['L', r'$\Gamma$', 'X', 'U', r'$\Gamma$'], fontsize=12)

plt.ylabel('Energy (eV)', fontsize=14)
plt.ylim(-13, 11)

plt.tight_layout()
plt.savefig("silicon_bands.png", dpi=200, bbox_inches='tight')
