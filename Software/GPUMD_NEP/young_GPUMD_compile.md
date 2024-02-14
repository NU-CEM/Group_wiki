module unload default-modules/2018
module unload apr-util/1.6.1
module unload apr/1.7.0
module unload gcc-libs
module load beta-modules
module load gcc-libs/10.2.0
module load cuda/11.3.1/gnu-10.2.0
git clone https://github.com/brucefan1983/GPUMD.git
cd GPUMD/src
make  
