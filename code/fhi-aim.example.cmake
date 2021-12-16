# Intel Compilers
set(CMAKE_Fortran_COMPILER "mpiifort" CACHE STRING "" FORCE)
set(CMAKE_Fortran_FLAGS "-O3 -ip -fp-model precise" CACHE STRING "" FORCE)
set(Fortran_MIN_FLAGS "-O0 -fp-model precise" CACHE STRING "" FORCE)
set(CMAKE_C_COMPILER "icc" CACHE STRING "" FORCE)
set(CMAKE_C_FLAGS "-O3 -ip -fp-model precise -std=gnu99" CACHE STRING "" FORCE)
set(LIB_PATHS "/cm/shared/apps/intel/compilers_and_libraries/2016.4.258/mkl/lib/intel64/" CACHE STRING "" FORCE)
set(LIBS "mkl_intel_lp64 mkl_sequential mkl_core mkl_blacs_intelmpi_lp64 mkl_scalapack_lp64" CACHE STRING "" FORCE)
set(USE_MPI ON CACHE BOOL "" FORCE)
set(USE_SCALAPACK ON CACHE BOOL "" FORCE)
set(USE_LIBXC ON CACHE BOOL "" FORCE)
set(USE_HDF5 OFF CACHE BOOL "" FORCE)
set(USE_RLSY ON CACHE BOOL "" FORCE)
set(ELPA2_KERNEL AVX2 CACHE STRING "Change to AVX/AVX2/AVX512 if running on Intel processors" FORCE)

# GNU Compilers
#set(CMAKE_Fortran_COMPILER ftn CACHE STRING "")
#set(CMAKE_Fortran_FLAGS "-O2 -fallow-argument-mismatch -ffree-line-length-none" CACHE STRING "")
#set(Fortran_MIN_FLAGS "-O0 -ffree-line-length-none" CACHE STRING "")
#set(CMAKE_C_COMPILER cc CACHE STRING "")
#set(CMAKE_C_FLAGS "-O2" CACHE STRING "")
#set(USE_MPI ON CACHE BOOL "" FORCE)
#set(USE_SCALAPACK ON CACHE BOOL "" FORCE)
#set(USE_LIBXC ON CACHE BOOL "" FORCE)
#set(USE_HDF5 OFF CACHE BOOL "" FORCE)
#set(USE_RLSY ON CACHE BOOL "" FORCE)

# Cray Compilers
#set(CMAKE_Fortran_COMPILER ftn CACHE STRING "")
#set(Fortran_MIN_FLAGS "-O0" CACHE STRING "")
#set(CMAKE_Fortran_FLAGS "-O3 -hfp3" CACHE STRING "")
#set(CMAKE_C_COMPILER cc CACHE STRING "")
#set(CMAKE_C_FLAGS "-O2 -funroll-loops -ffast-math" CACHE STRING "")
#set(USE_MPI ON CACHE BOOL "" FORCE)
#set(USE_SCALAPACK ON CACHE BOOL "" FORCE)
#set(USE_LIBXC ON CACHE BOOL "" FORCE)
