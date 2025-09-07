import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('graphene_bands.dat.gnu')

k = np.unique(data[:, 0])
bands = np.reshape(data[:, 1], (-1, len(k)))

for band in range(len(bands)):
    plt.plot(k, bands[band, :], linewidth=1, alpha=0.5, color='k')
plt.xlim(min(k), max(k))

# Fermi energy
plt.axhline(0.921, linestyle=(0, (8, 10)), linewidth=0.75, color='k', alpha=0.5)
# High symmetry k-points (check bands_pp.out)
plt.axvline(0.6667, linewidth=0.75, color='k', alpha=0.5)
plt.axvline(1, linewidth=0.75, color='k', alpha=0.5)
# text labels
plt.xticks(ticks= [0, 0.6667, 1, 1.5774], labels=[r'$\Gamma$', 'K', 'M', r'$\Gamma$'])
plt.ylabel("Energy (eV)")
plt.savefig("graphene.png", dpi=300)
#plt.show()
