Setup Archer2 for working with ase, calorine and (TODO) fhi-vibes

## Download Conda
```
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```

## Initialise Conda
```
~/miniconda3/bin/conda init bash
source ~/.bashrc
conda init
conda update -n base -c defaults conda
```

## Create environment and install dependencies
```
conda create -n calorine python=3.11
conda activate calorine
conda install pip
pip install ase calorine hiphive phonopy

```
