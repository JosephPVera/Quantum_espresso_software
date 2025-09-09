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

2. Installation tutorial
- https://www.youtube.com/watch?v=-5fcsJILc6U

3. Tutorial for running simulations
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
```bash
mpirun -np 4 pw.x -inp pw.scf.silicon.in > pw.scf.silicon.out
```

```bash
grep -e 'total energy' -e estimate pw.scf.silicon.out
```

- https://www-quantum--espresso-org.translate.goog/Doc/INPUT_PW.html?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc#idm401
- https://pranabdas.github.io/espresso/hands-on/graphene/

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


graphene: https://github.com/pranabdas/espresso/tree/main/src/graphene


### Using job script

https://uofsc-rc.github.io/tutorials/qe

### Visualize the crystal structure with xcrysden

```bash
xcrysden --pwi graphene_scf.in
```
