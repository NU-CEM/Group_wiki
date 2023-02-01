#!/bin/bash -l
# Slurm job options (job-name, compute nodes, job time)
#SBATCH --job-name=Example_MPI_Job
#SBATCH --time=06:00:00
#SBATCH --nodes=32
#SBATCH --tasks-per-node=64
#SBATCH --cpus-per-task=1

# Replace [budget code] below with your budget code (e.g. t01)
#SBATCH --account=e05-power-luc
#SBATCH --partition=standard
#SBATCH --qos=standard
#SBATCH --export=none
source /work/e05/e05/prakaya/fhi-vibes/bin/activate
module load cray-libsci
module swap PrgEnv-cray PrgEnv-gnu
export LD_LIBRARY_PATH=$CRAY_LD_LIBRARY_PATH:$LD_LIBRARY_PATH
logfile='run.log'

# timer
start_time="$(date -u +%s)"

for fol in qha_???.???
do echo Enter $fol
    cd $fol

    # perform phonopy calculation
    echo run phonopy
    vibes run phonopy >> $logfile
    echo "elapsed: $(($(date -u +%s)-$start_time))s"

    # perform postprocess
    vibes output phonopy phonopy/trajectory.son --full >> $logfile

    # perform reference aims calculation
    echo run aims
    vibes run singlepoint >> $logfile
    echo "elapsed: $(($(date -u +%s)-$start_time))s"
    # next
    cd ..
done
