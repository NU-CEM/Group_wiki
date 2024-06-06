#!/bin/bash -l
# Slurm job options (job-name, compute nodes, job time)
#SBATCH --job-name=Example_MPI_Job
#SBATCH --time=00:20:00
#SBATCH --nodes=16
#SBATCH --tasks-per-node=128
#SBATCH --cpus-per-task=1

# Replace [budget code] below with your budget code (e.g. t01)
#SBATCH --account=e05-power-luc
#SBATCH --partition=standard
#SBATCH --qos=short
#SBATCH --export=none
source /work/e05/e05/prakaya/fhi-vibes/bin/activate
module load cray-libsci
module swap PrgEnv-cray PrgEnv-gnu
export LD_LIBRARY_PATH=$CRAY_LD_LIBRARY_PATH:$LD_LIBRARY_PATH
logfile='run.log'

vibes run relaxation >> $logfile
