Compiling FHI-aims on Dade was even simpler than [compiling on Oswald](./aims_on_oswald.md) because of the [Intel oneAPI](https://www.intel.com/content/www/us/en/developer/tools/oneapi/toolkits.html#hpc-kit) available on Dade. 

1. Git clone from the aims repository
```
git clone https://aims-git.rz-berlin.mpg.de/aims/FHIaims.git
```
This requires an account on aims club and the git clone requires the users password. 

The nice thing about having the Intel oneAPI is that all the compilers are always latest and up to date. 

2. Create an empty `build` directory in the top level of the FHI-aims source code and `cd` into it

3. Create the relevant [cmake file](./code/fhi-aims.cmake.dade)

4. Run the cmake command 
``` cmake -C fhi-aims.cmake ..```
5. If all the compliers/libraries/dependencies are found and configured, run:
``` make -j 40```
where '40' is the number of cores assigned to compile the code. 

6. An aims binary should be ready as aims__scalapack.mpi.x copy this to a bin folder and use the binary from this location. 
As of 25th Jan 2022, the local version compiled on Dade is the '220115' version whereas on Oswald the version is '211206', but this shouldn't be a cause for alarm. 
