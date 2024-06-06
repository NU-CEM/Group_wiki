# Building NEP models with FHI-aims

GPUMD can be used to build Neuro Evolution Potential (NEP) models, and run MD using the resulting NEP model. This is, as the name suggests, ran on GPUs.

Calorine is used to extract energies and forces from the NEP model. This can be run on CPUs.

Furthermore, for building the NEP model using FHI-aims data, FHI-vibes is used to handle the jobs submission.

# LW to test

- [ ] Run n=6 NEP energy prediction and compare to DFT output

# To add to tutorial

- [ ] DFT input files for geometry relaxations and total energy single-point calculations (HSE06 and pbesol)
- [ ] Guidelines on ensuring the k-point density is consistent
- [ ] FHI-vibes setup using conda

# Training a NEP model with FHI-aims 

- See the Calorine tutorial [here](https://calorine.materialsmodeling.org/tutorials/generate_training_structures_and_training.html)
- Start with structures downloaded from Materials Project, for example. As tutorial highlights, create strained, deformed and rattled versions. Include rattles of supercells also.
- For training with fhi-aims, these will be exported as `geometry.in-n` files where `n` is a number to distinguish each structure. There is an example script for these last two steps.
- Create a fhi-vibes input file (see example) and slurm submission script (see example)
- Use the python script make_folders to create directories `calculation_n` corresponding to each structure, transfer across the required files (submit, fhi-vibes aims.in, geometry.in), and submit
- Submit each calculation to the supercomputer (currently this is done on a calculation-by-calculation basis)
- Transfer calculations across to the GPU(s) you are using for NEP model training
- Once complete, use the bash file to convert each output total energy to a formation energy
- Read in the energies and generate the sub-folders populated with NEP parameters and training data. There will be train/test split and one with all structures.
- Run the `nep` binary to train

## FHI-aims total energies for training a NEP model (or comparing against a NEP prediction)

NEP requires formation energies which are not automatically printed in the outfiles for fhi-aims. To convert from total energy to formation energy there is a script. CAUTION this is a hacky script which will overwrite your outfile, so use it on a copy!! This only works with ASE prior to June 2024. Oh yes, it only for Ba-Zr-S and it is specific to the calculation settings (xc functional etc). So you will need to re-create for the system you are interested in...

# Calorine for extracting predictions from a NEP model

## Predicting total energies and forces

- Calorine has functionality for extracting total energies and forces from NEP model
- this does not need GPU to run, it can be run on e.g. young head nodes.
- See the calorine tutorials on how to get energies and forces.
- You will need to install Calorine and ASE on whichever computer you are using, see [here](./setup_Young.md) for guidance how to install required dependancies via conda and pip.
- You will need the NEP model and the geometry you want to predict energies for.
- Take the NEP output and divide by number of atoms for comparison against the FHI-aims energy.

# Molecular Dynamics

## Creating `.xyz` files for MD simulations

- Make sure every geometry file in a conventional unit cell -- which means it should have orthogonal lattice vectors otherwise you tend to model weird cells.
- Run [the Python script](`write_xyz.py`) to generate a supercell of the desired size and export as a `.xyz`.
- [Sample conventional file](./BaZrS3_conventional.in) and the [resulting file](./model.xyz) in `.xyz` formatare provided.

## Running heating and cooling runs with GPUMD.

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


