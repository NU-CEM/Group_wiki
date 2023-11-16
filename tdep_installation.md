# TDEP installation on archer2/young

1. conda stuff:
```
conda create -n tdep python=3.10
conda activate tdep
conda install -c conda-forge gfortran openmpi-mpifort scalapack fftw hdf5
git clone https://github.com/tdep-developers/tdep.git
```
2. `cd` into the tdep repo. The [TDEP install](https://github.com/tdep-developers/tdep/blob/main/INSTALL.md) instruction comes with several `important_settings.xxx` files. In this installation, I use the conda settings by doing: 
```
cp important_settings.conda important_settings
``` 

3. Then I had to point to the conda installation by chaning the `PREFIX=/home/e05/e05/prakaya/miniconda3/envs/tdep` and change the `FCFLAGS="-ffree-line-length-none -std=f2008 -cpp -Wno-argument-mismatch"`:

4. Then to build:
```
./build_things.sh --nthreads_make 4
```

5. Afterwards I updated my `~/.bashrc` with the following:
```
MANPATH=$MANPATH:/path/to/tdep/man
PATH=$PATH:/path/to/tdep/bin
export MANPATH
export PATH
alias gnuplot='gnuplot -persist'
```
6. Install [tools.tdep](https://github.com/flokno/tools.tdep):
```
pip install https://github.com/flokno/tools.tdep/archive/main.zip
```


Note: for some apple silicon devices a `FCFLAGS_EXTRA="-L/Library/Developer/CommandLineTools//SDKs/MacOSX13.3.sdk/usr/lib/"` is needed. For my own laptop, I didn't need it. 🤔 More information (here)[https://github.com/tdep-developers/tdep/blob/main/INSTALL.md#Anaconda]
