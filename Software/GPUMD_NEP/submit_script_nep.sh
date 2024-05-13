#!/bin/bash -l
#$ -S /bin/bash
#$ -l h_rt=24:00:00
#$ -N Pingu
#$ -P Free
#$ -A MCC_power_luc
# no #$ -pe ppn=1 1
#$ -l gpu=2,mem=32G
#$ -cwd


# Run our MPI job. You can choose OpenMPI or IntelMPI for GCC.
module unload default-modules/2018
module unload apr-util/1.6.1
module unload apr/1.7.0
module unload gcc-libs
module load beta-modules
module load gcc-libs/10.2.0
module load cuda/11.3.1/gnu-10.2.0

./nep > out 
