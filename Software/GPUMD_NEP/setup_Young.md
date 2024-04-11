
```
module load python/miniconda3/4.10.3
source $UCL_CONDA_PATH/etc/profile.d/conda.sh
conda update -n base -c defaults conda
conda create -n nep python=3.11
conda activate nep
conda install cuda -c nvidia
pip install calorine 
pip install hiphive
pip install phonopy
```
