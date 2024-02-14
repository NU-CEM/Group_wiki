Compiling FHI-aims with modules available on Oswald

1. Git clone from the aims repository
```
git clone https://aims-git.rz-berlin.mpg.de/aims/FHIaims.git
```
This requires an account on aims club and the git clone requires the users password. 

Make sure cmake version is > 3.10. New versions can easily be installed through conda. 
```
conda install -c anaconda cmake
```
2. Load the intel compilers, intel MPI libraries and Intel Maths Kernal Libraries
```
module load openmpi/intel-opa/intel-hfi/64/1.10.4
module load intel/mpi/64/5.1.3/2016.4.258
module load intel/compiler/64/16.0.4/2016.4.258
module load intel/mkl/64/11.3.4/2016.4.258
```
3. Create an empty `build` directory in the top level of the FHI-aims source code and `cd` into it

3. Create the relevant [cmake file](../code/fhi-aims.cmake)

4. Run the cmake command 
``` cmake -C fhi-aims.cmake ..```
5. If all the compliers/libraries/dependencies are found and configured, run:
``` make -j 6```
where '6' is the number of cores assigned to compile the code. 

6. An aims binary should be ready as aims__scalapack.mpi.x copy this to a bin folder and use the binary from this location. 
Note: I've had to redo this process for the new Oswald nodes. The new nodes require the binary to be compiled in the new compute nodes. :face_with_rolling_eyes: Simply ssh compute033 and entre the password to enter the new nodes. 
