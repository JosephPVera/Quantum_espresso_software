# Quantum Espresso Software

## How install it?

1. Requirements:
   ```bash
   sudo apt update
   sudo apt install build-essential gfortran gcc g++ \
   libopenmpi-dev openmpi-bin \
   libblas-dev liblapack-dev libfftw3-dev \
   git wget make
   ```
2. Download the [qe-7.4.1](https://github.com/JosephPVera/Quantum_espresso_software/tree/main/qe-7.4.1) file using
   ```bash
   git clone https://github.com/JosephPVera/Quantum_espresso_software.git
   ```
3. Set up the .bashrc file similar to [bashrc](https://github.com/JosephPVera/Quantum_espresso_software/blob/main/bashrc), write 
   ```bash
   # Quantum Espresso
   PATH="/home/joseph/qe-7.4.1/bin:$PATH"
   ```  
4. Run
   ```bash
   source ~/.bashrc
   ```
5. Now you can use the software.
   
## Install from the scratch

1. Installation tutorial
- https://www.youtube.com/watch?v=-5fcsJILc6U

2. Tutorial for running simulations
- https://github.com/rpadhikari/Himachal_NMM_22
- https://pranabdas.github.io/espresso/category/hands-on/
- https://jyhuang.idv.tw/JYH_QESimulation.html
- https://www.youtube.com/watch?v=gVHrjbDCxaM&list=PL6fYKYtuMec_2-_18mxoHswOoCMz3KTe4&index=6



--- 
Run SCF simulation
            
Importante: https://pranabdas.github.io/espresso/category/hands-on/
---

```bash
pw.x < pw.scf.silicon.in > pw.scf.silicon.out
```
### For parallel execution

https://www.youtube.com/watch?v=2PAJGrNhZB8

Activate parallelization
```bash
./configure
```

```bash
make pw
```

```bash
make pwall
```

check the number of cores:
```bash
lscpu
```

Run 
```bash
mpirun -np 4 pw.x -inp grap_SOC_scf.in > grap_SOC_scf.out
```

```bash
grep -e 'total energy' -e estimate pw.scf.silicon.out
```

- PW: https://www.quantum-espresso.org/Doc/INPUT_PW.html
- DOS: https://www.quantum-espresso.org/Doc/INPUT_DOS.html
- BANDS: https://www.quantum-espresso.org/Doc/INPUT_BANDS.html
- PROJWFC: https://www.quantum-espresso.org/Doc/INPUT_PROJWFC.html
- pp.x: https://www.quantum-espresso.org/Doc/INPUT_PP.html
- https://pranabdas.github.io/espresso/hands-on/graphene/

- Band gap: https://mattermodeling.stackexchange.com/questions/12440/how-to-find-the-band-gap-energy-value-in-quantum-espresso
- SOC: https://www.quantum-espresso.org/Doc/pw_user_guide/node10.html
  
### Pseudopotentials: 

useful information: https://pranabdas.github.io/espresso/setup/pseudo-potential/

- https://pseudopotentials.quantum-espresso.org/legacy_tables
- https://dalcorso.github.io/pslibrary/
- https://www.pseudo-dojo.org/
- https://pseudopotentials.quantum-espresso.org/
- https://www.materialscloud.org/discover/sssp/table/efficiency
- https://www.physics.rutgers.edu/gbrv/
- https://nninc.cnf.cornell.edu
- http://www.quantum-simulation.org/potentials/
- BLYP pseudopotentials: https://pseudopotentials.quantum-espresso.org/legacy_tables/hartwigesen-goedecker-hutter-pp
- SCAN pseudopotentials: https://yaoyi92.github.io/scan-tm-pseudopotentials.html
  
- Carbono: https://pseudopotentials.quantum-espresso.org/legacy_tables/ps-library/c
- Carbono: https://nninc.cnf.cornell.edu/psplist.php?element=c


graphene: https://github.com/pranabdas/espresso/tree/main/src/graphene


### Using job script

- https://uofsc-rc.github.io/tutorials/qe

### Visualize the crystal structure with xcrysden

Install xcrysden : 

- https://github.com/JosephPVera/Exciting_code_software/tree/main/xcrysden_solutions

```bash
xcrysden --pwi graphene_scf.in
```

###    Find the gap

- https://mattermodeling.stackexchange.com/questions/12440/how-to-find-the-band-gap-energy-value-in-quantum-espresso

## Modifying the resolution 
### 1. in /home/joseph/qe-7.4.1/PP/src/dos.f90
Change the resolution in section:
```bash
WRITE (4,'(f15.8,3e20.10)') E * rytoev, DOSofE(1)/rytoev, DOSint(1)
```

update the dos.90 in /home/joseph/qe-7.4.1 using
```bash
make pwall -j2
```

### 2. in /home/joseph/qe-7.4.1/PP/src/bands.f90
Change the resolution in section:
```bash
WRITE( stdout,'(5x,"high-symmetry point: ",3f7.4,&
                 &"   x coordinate",f9.4)') (xk(i,n),i=1,3), kx(n)
```

and 
```bash
WRITE (iunpun0,'(2f10.4)') (kx(n), et(i,n),n=nks1tot,nks2tot)
```

update the bands.90 in /home/joseph/qe-7.4.1 using
```bash
make pwall -j2
```

### 3. in /home/joseph/qe-7.4.1/PW/src/print_ks_energies.f90
Change the resolution in section:
```bash
9040 FORMAT(/'     the Fermi energy is ',F10.4,' ev' )
```

update the print_ks_energies.f90 in /home/joseph/qe-7.4.1 using
```bash
make pw -j2
```

# Commands to run the simulations
### SCF
```bash
pw.x -i grap_scf.in > grap_scf.out
```

Parallel
```bash
mpirun -np 6 pw.x -inp grap_scf.in > grap_scf.out
```

### NSCF
```bash
pw.x -i grap_nscf.in > grap_nscf.out
```

Parallel
```bash
mpirun -np 6 pw.x -inp grap_nscf.in > grap_nscf.out
```

### DOS
```bash
dos.x -i grap_dos.in > grap_dos.out
```

Parallel
```bash
mpirun -np 6 dos.x -inp grap_dos.in > grap_dos.out
```

### PDOS
```bash
projwfc.x < grap_projwfc.in > grap_projwfc.out
```

Parallel
```bash
mpirun -np 6 projwfc.x -inp < grap_projwfc.in > grap_projwfc.out
```

### Band structure
```bash
pw.x -i grap_bands.in > grap_bands.out
```

```bash
bands.x -i grap_bands_pp.in > grap_bands_pp.out
```

Parallel
```bash
mpirun -np 6 pw.x -inp grap_bands.in > grap_bands.out
```

```bash
mpirun -np 6 bands.x -inp grap_bands_pp.in > grap_bands_pp.out
```

### Electric Potential
```bash
pp.x < pp_SOC_rashba.in> pp_SOC_rashba.out
```

Parallel
```bash
mpirun -np 6 pp.x -inp < pp_SOC_rashba.in > pp_SOC_rashba.out
```

### Data to plot the electric potential
```bash
average.x <average.in> average.out
```

Parallel
```bash
mpirun -np 6 average.x -inp <average.in> average.out
```
