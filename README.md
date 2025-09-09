# Quantum_espresso_softwareh

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

https://www-quantum--espresso-org.translate.goog/Doc/INPUT_PW.html?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc#idm401


https://pranabdas.github.io/espresso/hands-on/graphene/

pseudopotential: 
- https://pseudopotentials.quantum-espresso.org/legacy_tables
- https://dalcorso.github.io/pslibrary/
- https://www.pseudo-dojo.org/
- https://pseudopotentials.quantum-espresso.org/

graphene: https://github.com/pranabdas/espresso/tree/main/src/graphene


## Using job script

https://uofsc-rc.github.io/tutorials/qe
