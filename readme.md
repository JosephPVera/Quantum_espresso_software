# Quantum Espresso Software

## 1. How install it?

### 1.1. Using the source package from the official website: https://www.quantum-espresso.org/
- [x] Installation tutorial: https://www.youtube.com/watch?v=-5fcsJILc6U
- [x] Some tutorials:
  - https://github.com/rpadhikari/Himachal_NMM_22
  - https://pranabdas.github.io/espresso/category/hands-on/
  - https://jyhuang.idv.tw/JYH_QESimulation.html
  - https://www.youtube.com/watch?v=gVHrjbDCxaM&list=PL6fYKYtuMec_2-_18mxoHswOoCMz3KTe4&index=6

### 1.2. Using the [qe-7.4.1](https://github.com/JosephPVera/Quantum_espresso_software/tree/main/qe-7.4.1) file (compiled version)
1. Install the requirements
   ```bash
   sudo apt update
   sudo apt install build-essential gfortran gcc g++ \
   libopenmpi-dev openmpi-bin \
   libblas-dev liblapack-dev libfftw3-dev \
   git wget make
   ```
2. Install Git
   ```bash
   sudo apt update
   sudo apt install git
   git --version
   ```   
3. Download the [Quantum_espresso_software](https://github.com/JosephPVera/Quantum_espresso_software) repository
   ```bash
   git clone https://github.com/JosephPVera/Quantum_espresso_software.git
   ```
4. Copy the [qe-7.4.1](https://github.com/JosephPVera/Quantum_espresso_software/tree/main/qe-7.4.1) file to **/home/joseph**
   ```bash
   cp -r Quantum_espresso_software/qe-7.4.1 .
   ```
5. Set up the **.bashrc** file on your laptop or pc similar to [bashrc](https://github.com/JosephPVera/Quantum_espresso_software/blob/main/bashrc) file 
   ```bash
   # Quantum Espresso
   PATH="/home/joseph/qe-7.4.1/bin:$PATH"
   ```  
6. Run
   ```bash
   source ~/.bashrc
   ```
7. Create the job folder
   ```bash
   mkdir /home/joseph/Documents/qe
   ```
8. Copy the **pseudos** folder and create a folder of your choice to work in, for example the **silicon** folder
   ```bash
   cp -r /home/joseph/Quantum_espresso_software/Examples/pseudos /home/joseph/Documents/qe
   mkdir /home/joseph/Documents/qe/silicon
   ```
9. Now you can use the software.

**Information:** This compiled version of Quantum ESPRESSO does not have parallel calculation enabled.

## 2. Enabling parallel execution
Check: https://www.youtube.com/watch?v=2PAJGrNhZB8

2.1. Activate parallelization
```bash
./configure
```
2.2. Run
```bash
make pw
```
2.3. Run
```bash
make pwall
```
2.4. Check the number of cores on your laptop or pc
```bash
lscpu
```

## 3. Replicating the example in the [silicon](https://github.com/JosephPVera/Quantum_espresso_software/tree/main/Examples/silicon) file
3.1. Copy the files with the .in extension into the **silicon** file
```bash
cp /home/joseph/Quantum_espresso_software/Examples/silicon/silicon_*.in /home/joseph/Documents/qe/silicon/
cd /home/joseph/Documents/qe/silicon/
```
3.2. Run the SCF calculation 
```bash
mpirun -np 4 pw.x -inp silicon_scf.in > silicon_scf.out
```
3.3. Check the total energy of the system
```bash
grep -e 'total energy' -e estimate silicon_scf.out
```
3.4. Run the NSCF calculation
```bash
mpirun -np 4 pw.x -inp silicon_nscf.in > silicon_nscf.out
```
3.5. Check the VBM and CBM values. Calculate the band gap as **gap = CBM - VBM**
```bash
grep 'highest occupied' silicon_nscf.out
```
3.6. Run the DOS calculation and plot it
```bash
mpirun -np 4 dos.x -inp silicon_dos.in > silicon_dos.out
```
3.7. Run the PDOS calculation and plot it 
```bash
mpirun -np 4 projwfc.x -inp silicon_projwfc.in > silicon_projwfc.out
```
3.7. Run the BAND calculation and plot it
```bash
mpirun -np 4 pw.x -inp silicon_bands.in > silicon_bands.out
```
```bash
mpirun -np 4 bands.x -inp silicon_bands_pp.in > silicon_bands_pp.out
```
## 4. Input File Description: Check the tags to set up the files with the .in extension
- [x] PW: https://www.quantum-espresso.org/Doc/INPUT_PW.html
- [x] DOS: https://www.quantum-espresso.org/Doc/INPUT_DOS.html
- [x] PROJWFC: https://www.quantum-espresso.org/Doc/INPUT_PROJWFC.html
- [x] BANDS: https://www.quantum-espresso.org/Doc/INPUT_BANDS.html
- [x] pp.x: https://www.quantum-espresso.org/Doc/INPUT_PP.html
  
## 5. Pseudopotentials
Useful information: https://pranabdas.github.io/espresso/setup/pseudo-potential/

- [x] https://pseudopotentials.quantum-espresso.org/legacy_tables
- [x] https://dalcorso.github.io/pslibrary/
- [x] https://www.pseudo-dojo.org/
- [x] https://pseudopotentials.quantum-espresso.org/
- [x] https://www.materialscloud.org/discover/sssp/table/efficiency
- [x] https://www.physics.rutgers.edu/gbrv/
- [x] https://nninc.cnf.cornell.edu
- [x] http://www.quantum-simulation.org/potentials/
- [x] BLYP pseudopotentials: https://pseudopotentials.quantum-espresso.org/legacy_tables/hartwigesen-goedecker-hutter-pp
- [x] SCAN pseudopotentials: https://yaoyi92.github.io/scan-tm-pseudopotentials.html
  
- [x] Carbono: https://pseudopotentials.quantum-espresso.org/legacy_tables/ps-library/c
- [x] Carbono: https://nninc.cnf.cornell.edu/psplist.php?element=c

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
- https://pranabdas.github.io/espresso/hands-on/graphene/
- Band gap: https://mattermodeling.stackexchange.com/questions/12440/how-to-find-the-band-gap-energy-value-in-quantum-espresso
- SOC: https://www.quantum-espresso.org/Doc/pw_user_guide/node10.html
- graphene: https://github.com/pranabdas/espresso/tree/main/src/graphene

  
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
### 1. SCF
```bash
pw.x -i grap_scf.in > grap_scf.out
```

Parallel
```bash
mpirun -np 6 pw.x -inp grap_scf.in > grap_scf.out
```

### 2. NSCF
```bash
pw.x -i grap_nscf.in > grap_nscf.out
```

Parallel
```bash
mpirun -np 6 pw.x -inp grap_nscf.in > grap_nscf.out
```

### 3. DOS
```bash
dos.x -i grap_dos.in > grap_dos.out
```

Parallel
```bash
mpirun -np 6 dos.x -inp grap_dos.in > grap_dos.out
```

### 4. PDOS
```bash
projwfc.x < grap_projwfc.in > grap_projwfc.out
```

Parallel
```bash
mpirun -np 6 projwfc.x -inp grap_projwfc.in > grap_projwfc.out
```

### 5. Band structure
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

### 6. Electric Potential
```bash
pp.x < pp_SOC_rashba.in> pp_SOC_rashba.out
```

Parallel
```bash
mpirun -np 6 pp.x -inp < pp_SOC_rashba.in > pp_SOC_rashba.out
```

### 7. Data to plot the electric potential
```bash
average.x <average.in> average.out
```

Parallel
```bash
mpirun -np 6 average.x -inp <average.in> average.out
```
