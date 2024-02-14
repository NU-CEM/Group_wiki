New year (of the PhD), new HPC. 

Following are the instructions for compiling aims in Young

1. Git clone from the aims repo:
```
git clone https://aims-git.rz-berlin.mpg.de/aims/FHIaims.git
```
2. Create an empty `build` directory in the top level of the FHI-aims source code and `cd` into it

3. Create the relevant [cmake file](../FHI-aims_Compilation/fhi-aims.cmake.young)

4. Run the cmake command 
``` cmake -C fhi-aims.cmake ..```
5. If all the compliers/libraries/dependencies are found and configured, run:
``` make -j 16```

6. An aims binary should be ready as aims__scalapack.mpi.x copy this to a `bin` folder and use the binary from this location. 
