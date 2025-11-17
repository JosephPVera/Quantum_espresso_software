#!/usr/bin/env python3
# Written by Joseph P.Vera
# 2024-11

import matplotlib.pyplot as plt
from matplotlib import rcParamsDefault
import numpy as np

VBM = 6.2107

# load data
def data_loader(fname):
    import numpy as np

    data = np.loadtxt(fname)
    
    # Rescale energy with respect to the VBM
    energy = data[:, 0] - VBM
    
    pdos = data[:, 1]  # ldos col, total contribution for a given orbital

    return energy, pdos

energy, pdos_s = data_loader('silicon_pdos.dat.pdos_atm#1(Si)_wfc#1(s)')
_, pdos_p = data_loader('silicon_pdos.dat.pdos_atm#1(Si)_wfc#2(p)')

#plots
plt.plot(energy, pdos_s, linewidth=1, color='xkcd:green', label='s-orbital')
plt.plot(energy, pdos_p, linewidth=1, color='xkcd:blue', label='p-orbital')

plt.xlabel('Energy (eV)', fontsize=14)
plt.ylabel('DOS (States/eV)', fontsize=14)

plt.xlim(-13, 10)
plt.ylim(0, 1)

plt.legend()
plt.tight_layout()
plt.savefig("silicon_pdos-atom_1.png", dpi=300)
