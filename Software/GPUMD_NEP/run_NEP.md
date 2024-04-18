```
ssh young
module load python/miniconda3/4.10.3
source $UCL_CONDA_PATH/etc/profile.d/conda.sh
conda activate nep
```

You need to have:
- nep.txt (nep model)
- run.in (simulation settings)
- structure.xyz (atoms file)

The executable is stored within GPUMD
```
/home/mmm0117/GPUMD/src/gpumd
```
