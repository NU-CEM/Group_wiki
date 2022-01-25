## FHI-aims: The basics

- There are only two main input files in aims, geometry.in and control.in
- The geometry.in file is the POSCAR analogue of VASP which contains the lattice parameters and atomic positions in Cartesian space. 
- The control.in file is the INCAR, KPOINTS and POTCAR combined. The file contains the DFT settings (functional and SCF convergence criteria) and kpoints and the atomic species files. 
- For production runs, species files are generally "tight" settings and can be internally tightened with the tight-tier1 or tight-deafult and tight-tier2 options. 
- Unlike VASP, input keywords/species in the control.in are insentive to ordering from the geometry.in files. The k-grids by default are Gamma-centered. 
