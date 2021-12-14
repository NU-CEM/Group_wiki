# Compiling FHI-Aims on Oswald

## Approach 1 - conda

1. Create a suitable conda environment
  - `conda create --name aims-env python=3.8`
  - `conda activate aims-env` (note before doing this you may need to follow the prompts to `conda init bash`, logout, then log back in again)
  - `conda install -c conda-forge git pip zip cmake` 
  - `conda install -c conda-forge numpy scipy matplotlib ase`
  - `conda install -c anaconda mkl` 
  - `conda install -c conda-forge openmpi-mpifort`
  - `conda install -c conda-forge scalapack`

2. Create an empty `build` directory in the top level of the FHI-aims source code and `cd` into it

3. Create the relevant [cmake file](./code/fhi-aims.conda.cmake)

4. cmake -C initial_cache.conda.cmake ..

Currently there is a problem: `CMake Error: File /home/osw_mynf8/fhi-aims.210716_2/esl/elsi/.elsi.pc.in does not exist.`

## Approach 2 - modules

1. Load the intel compilers, intel MPI libraries and Intel Maths Kernal Libraries
```module load intel/compiler/64/16.0.4/2016.4.258
module load intel/mpi/64/5.1.3/2016.4.258
module load intel/mkl/64/11.3.4/2016.4.258
```

2. Create an empty `build` directory in the top level of the FHI-aims source code and `cd` into it

3. Create the relevant [cmake file](./code/fhi-aim.example.cmake)

4. cmake -C initial_cache.conda.cmake ..

Currently there is a problem: `CMake Error: File /home/osw_mynf8/fhi-aims.210716_2/esl/elsi/.elsi.pc.in does not exist.`
