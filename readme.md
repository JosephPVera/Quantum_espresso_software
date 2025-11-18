# Quantum Espresso Software

## 0. Quantum ESPRESSO workflow
![Alt text](https://github.com/JosephPVera/Quantum_espresso_software/blob/main/Examples/workflow/qe-workflow.png)

## 1. How install it?

### 1.1. Using the source package from the official website: https://www.quantum-espresso.org/
- [x] Installation tutorial: https://www.youtube.com/watch?v=-5fcsJILc6U
- [x] Some tutorials:
  - https://github.com/rpadhikari/Himachal_NMM_22
  - https://pranabdas.github.io/espresso/category/hands-on/
  - https://jyhuang.idv.tw/JYH_QESimulation.html
  - https://www.youtube.com/watch?v=gVHrjbDCxaM&list=PL6fYKYtuMec_2-_18mxoHswOoCMz3KTe4&index=6

### 1.2. Using the [qe-7.4.1](https://github.com/JosephPVera/Quantum_espresso_software/tree/main/qe-7.4.1) folder (compiled version)
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
4. Copy the [qe-7.4.1](https://github.com/JosephPVera/Quantum_espresso_software/tree/main/qe-7.4.1) folder to **/home/joseph/**
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
cd /home/joseph/qe-7.4.1
./configure
```
2.2. Run
```bash
make pw
```
```bash
make pwall
```
2.3. Check the number of cores on your laptop or pc
```bash
lscpu
```

## 3. Replicating the example in the [silicon](https://github.com/JosephPVera/Quantum_espresso_software/tree/main/Examples/silicon) file
3.0. **Warning:** Keep in mind that this case is just an example; for reliable and accurate calculations, it is essential to begin with convergence tests and relax the system.

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
3.5. Check the VBM and CBM values
```bash
grep 'highest occupied' silicon_nscf.out
```
This command will print a line like the following
```bash
highest occupied, lowest unoccupied level (ev):     6.2107    6.7835
```
Calculate the band gap as **gap = CBM - VBM**
```bash
Gap = 6.7835 - 6.2107 = 0.5728 eV
```

3.6. Run the DOS calculation
```bash
mpirun -np 4 dos.x -inp silicon_dos.in > silicon_dos.out
```
3.7. Plot the DOS using the [dos.py](https://github.com/JosephPVera/Quantum_espresso_software/blob/main/Examples/bin/dos.py) script
![Alt text](https://github.com/JosephPVera/Quantum_espresso_software/blob/main/Examples/silicon/silicon_dos.png)

3.8. Run the PDOS calculation 
```bash
mpirun -np 4 projwfc.x -inp silicon_projwfc.in > silicon_projwfc.out
```
3.9. Plot the PDOS using the [pdos.py](https://github.com/JosephPVera/Quantum_espresso_software/blob/main/Examples/bin/pdos.py) script
![Alt text](https://github.com/JosephPVera/Quantum_espresso_software/blob/main/Examples/silicon/silicon_pdos-atom_1.png)

3.10. Run the BAND calculation
```bash
mpirun -np 4 pw.x -inp silicon_bands.in > silicon_bands.out
```
```bash
mpirun -np 4 bands.x -inp silicon_bands_pp.in > silicon_bands_pp.out
```

3.11. Plot the band structure using the [bandplot.py](https://github.com/JosephPVera/Quantum_espresso_software/blob/main/Examples/bin/bandplot.py) script
![Alt text](https://github.com/JosephPVera/Quantum_espresso_software/blob/main/Examples/silicon/silicon_bands.png)

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

## 6. Visualize the crystal structure 
### 6.1. [xcrysden](http://www.xcrysden.org/)
6.1.1. Install xcrysden
```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install xcrysden
```
6.1.2. Visualize
```bash
xcrysden --pwi silicon_scf.in
```

**WARNING:** If xcrysden crashes with error, use these steps to fix it

6.1.3. Copy **custom-definitions** file
```bash
mkdir .xcrysden
cd .xcrysden
cp /usr/share/xcrysden/Tcl/custom-definitions .
```

6.1.4. Uncommenting the following line in the **custom_definitions** file
```bash
#set toglOpt(accum) false
```

### 6.2. [VESTA](https://jp-minerals.org/vesta/en/)
6.2.1. Download VESTA

6.2.2. Unpack the file in the path **/home/joseph/Downloads**
```bash
tar -xvjf VESTA-gtk3.tar.bz2
```
6.2.3. Copy to the **/home/joseph/**
```bash
cp -r VESTA-gtk3 ../VESTA
```
6.2.4. Set up the **.bashrc** file on your laptop or pc similar to [bashrc](https://github.com/JosephPVera/Quantum_espresso_software/blob/main/bashrc) file 
```bash
alias vesta="/home/joseph/VESTA/VESTA"
```
6.2.5. Run
```bash
source ~/.bashrc
```

6.2.5. Download the [qe_convert.py](https://github.com/JosephPVera/Quantum_espresso_software/blob/main/Examples/bin/qe_convert.py) script

6.2.6. Run
```bash
qe_convert.py silicon_scf.in
```
6.2.7. Visualize
```bash
vesta POSCAR
```

## 7. Extra information
  
### 7.1. Find the gap

- https://mattermodeling.stackexchange.com/questions/12440/how-to-find-the-band-gap-energy-value-in-quantum-espresso

### 7.2. Using job script in HPC
- https://uofsc-rc.github.io/tutorials/qe

### 7.3. Another example: Graphene
- https://pranabdas.github.io/espresso/hands-on/graphene/
- https://github.com/pranabdas/espresso/tree/main/src/graphene
- SOC: https://www.quantum-espresso.org/Doc/pw_user_guide/node10.html
  
## 8. Modifying the resolution 
### 8.1. DOS: /home/joseph/qe-7.4.1/PP/src/dos.f90
Change the resolution in section:
```bash
WRITE (4,'(f15.8,3e20.10)') E * rytoev, DOSofE(1)/rytoev, DOSint(1)
```

update the **dos.90** file in **/home/joseph/qe-7.4.1** using
```bash
make pwall -j2
```

### 8.2. BANDS: /home/joseph/qe-7.4.1/PP/src/bands.f90
Change the resolution in section:
```bash
WRITE( stdout,'(5x,"high-symmetry point: ",3f7.4,&
                 &"   x coordinate",f9.4)') (xk(i,n),i=1,3), kx(n)
```

and 
```bash
WRITE (iunpun0,'(2f10.4)') (kx(n), et(i,n),n=nks1tot,nks2tot)
```

update the **bands.90** file in **/home/joseph/qe-7.4.1** using
```bash
make pwall -j2
```

### 8.3. Fermy energy: /home/joseph/qe-7.4.1/PW/src/print_ks_energies.f90
Change the resolution in section:
```bash
9040 FORMAT(/'     the Fermi energy is ',F10.4,' ev' )
```

update the **print_ks_energies.f90** file in **/home/joseph/qe-7.4.1** using
```bash
make pw -j2
```

## 9. Commands to run the simulations
### 9.1. SCF
```bash
pw.x -i grap_scf.in > grap_scf.out
```

Parallel
```bash
mpirun -np 6 pw.x -inp grap_scf.in > grap_scf.out
```

### 9.2. NSCF
```bash
pw.x -i grap_nscf.in > grap_nscf.out
```

Parallel
```bash
mpirun -np 6 pw.x -inp grap_nscf.in > grap_nscf.out
```

### 9.3. DOS
```bash
dos.x -i grap_dos.in > grap_dos.out
```

Parallel
```bash
mpirun -np 6 dos.x -inp grap_dos.in > grap_dos.out
```

### 9.4. PDOS
```bash
projwfc.x < grap_projwfc.in > grap_projwfc.out
```

Parallel
```bash
mpirun -np 6 projwfc.x -inp grap_projwfc.in > grap_projwfc.out
```

### 9.5. Band structure
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

### 9.6. Electric Potential
```bash
pp.x < pp_SOC_potential.in> pp_SOC_potential.out
```

Parallel
```bash
mpirun -np 6 pp.x -inp < pp_SOC_potential.in > pp_SOC_potential.out
```

### 9.7. Data to plot the electric potential
```bash
average.x <average.in> average.out
```
