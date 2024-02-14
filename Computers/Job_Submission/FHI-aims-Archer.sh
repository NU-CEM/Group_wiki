#!/bin/bash

# Slurm job options (job-name, compute nodes, job time)
#SBATCH --job-name=Example_MPI_Job
#SBATCH --time=24:00:00
#SBATCH --nodes=16
#SBATCH --tasks-per-node=128
#SBATCH --cpus-per-task=1

# Replace [budget code] below with your budget code (e.g. t01)
#SBATCH --account=e05-react-wal
#SBATCH --partition=standard
#SBATCH --qos=standard
#SBATCH --export=none

# Load compilation time environment
module load cpe/21.09
module swap PrgEnv-cray PrgEnv-gnu
export LD_LIBRARY_PATH=$CRAY_LD_LIBRARY_PATH:$LD_LIBRARY_PATH

# Set the number of threads to 1
#   This prevents any threaded system libraries from automatically
#   using threading.
export OMP_NUM_THREADS=1

# Launch the parallel job
#   Using 512 MPI processes and 128 MPI processes per node
#   srun picks up the distribution from the sbatch options
ulimit -s unlimited

srun --cpu-bind=cores /work/e05/e05/shared/wmd_shared/Binaries/Aims/Jun22/Gnu/aims.220609.scalapack.mpi.x > aims.out
