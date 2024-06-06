#!/bin/bash -l 
  
module load cpe/21.09
module swap PrgEnv-cray PrgEnv-gnu
export LD_LIBRARY_PATH=$CRAY_LD_LIBRARY_PATH:$LD_LIBRARY_PATH
export OMP_NUM_THREADS=1
ulimit -s unlimited
source /work/e05/e05/prakaya/fhi-vibes/bin/activate

srun -distribution=block:block --hint=nomultithread /work/e05/e05/prakaya/chalcogenide_perovskites/aims.220619.scalapack.mpi.x
