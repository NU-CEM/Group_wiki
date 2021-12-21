Compiling FHI-aims with modules available on Oswald

1. Git clone from the aims repository
```
git clone https://aims-git.rz-berlin.mpg.de/aims/FHIaims.git
```
This requires an account on aims club and the git clone requires the users password. 

2. Load the intel compilers, intel MPI libraries and Intel Maths Kernal Libraries
```
module load intel/compiler/64/2017/17.0.6 
module load intel/mpi/64/2017/6.256 
module load intel/mkl/64/2017/6.256 
```
Note: the 2016 libraries tried in a [previous approach](./compiling_aims.md) results in a compilation error "src/external/M_strings/M_strings.f90(8087): error #8798: The construct name in the EXIT statement does not match any DO or BLOCK construct to which the EXIT statement belongs."

The 2017 libraries work fine but we much check if the latest intel compliers ans libraries can be installed on oswald as well.

3. Create an empty `build` directory in the top level of the FHI-aims source code and `cd` into it

3. Create the relevant [cmake file](./code/fhi-aims.cmake)

4. Run the cmake command 
``` cmake -C fhi-aims.cmake ..```
5. If all the compliers/libraries/dependencies are found and configured, run:
``` make -j 6```
where '6' is the number of cores assigned to compile the code. 

6. An aims binary should be ready as aims__scalapack.mpi.x copy this to a bin folder and use the binary from this location. 
