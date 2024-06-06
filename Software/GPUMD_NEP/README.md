# Heating/Cooling runs

To run molecular dynamics, use the [run.in](https://github.com/NU-CEM/Group_wiki/blob/main/Software/GPUMD_NEP/run.in) file, the [submit_GPUMD](https://github.com/NU-CEM/Group_wiki/blob/main/Software/GPUMD_NEP/submit_script_gpumd.sh) file and specify the geometry using an extended xyz file (`.exyz`). 
It assumes that the `gpumd` binary is in the same folder.

Following is the meaning of all the lines in the `run.in` file:
1. `potential` - location of the `nep.txt`
2. `velocity` -  (units of K) initial velocity given to the system. For heating runs, this starts from 1K and for cooling runs, you can start from say, 1200K or 1500K
3. `timestep` - (units of fs) 1 femtosecond (I never change this)
4. `ensemble` - `npt_scr` (for thermodynamic integration, use `nvt` and constant volume) `1 1200` is the temp range, `100` is the T_coupling (I've never varied this), `0 0 0 0 0 0` these are pressure parameters in a triclinic cell, and `100 100 100 100 100 100` are the elstic constants in a triclinic cell and finally, `1000` is the is the P_coupling (I've never varied this)     
5. `dump_exyz` - `100000 1 1 1` dumps extended xyz every 10000 steps (useful for visualization)
6. `dump_thermo` - `100000` dumps thermo file every 1000 steps (all useful thermodynamic quantities are here)
7. `run` - (units of fs) `50000000` (this is 50 ns) 

## Creating `.xyz` files for MD simulations

- Make sure every geometry file in a conventional unit cell -- which means it should have orthogonal lattice vectors otherwise you tend to model weird cells.
- Run [the Python script](`write_xyz.py`) to generate a supercell of the desired size and export as a `.xyz`.
- [Sample conventional file](./BaZrS3_conventional.in) and the [resulting file](./model.xyz) in `.xyz` formatare provided.

## To add

- [ ] DFT input files for geometry relaxations and total energy single-point calculations (HSE06 and pbesol)
- [ ] Guidelines on ensuring the k-point density is consistent

## FHI-aims total energies for training a NEP model, and comparison with NEP output

NEP requires formation energies which are not automatically printed in the outfiles for fhi-aims. To convert from total energy to formation energy there is a script. CAUTION this is a hacky script which will overwrite your outfile, so use it on a copy!! This only works with ASE prior to June 2024. This is open source software, baby.

## Calculating total energies and forces using an existing NEP model

- Calorine has functionality for extracting total energies and forces from NEP model
- this does not need GPU to run, it can be run on e.g. young head nodes.
- See the calorine tutorials on how to get energies and forces.
- You will need to install Calorine and ASE on whichever computer you are using.


