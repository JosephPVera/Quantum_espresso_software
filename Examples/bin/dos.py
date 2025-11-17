#!/usr/bin/env python3
# Written by Joseph P.Vera
# 2024-11

import numpy as np
import matplotlib.pyplot as plt

VBM =   6.2107

# Load data, skipping the first line (header)
data = np.loadtxt('silicon_dos.dat', comments='#')

# Rescale energy with respect to the VBM
energy = data[:, 0] - VBM

# DOS
dos = data[:, 1]

# Plot
plt.plot(energy, dos, color='xkcd:blue', linewidth=1)
plt.xlabel('Energy (eV)', fontsize=14)
plt.ylabel('DOS (States/eV)', fontsize=14)

plt.xlim(-13, 10)
plt.ylim(0, 2.5)

plt.tight_layout()
plt.savefig("silicon_dos.png", dpi=300)
