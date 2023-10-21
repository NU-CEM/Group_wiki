This is a collection of my notes for the TDEP (temperature-dependent effective potential) method. Installation instructions are [here](). Also install the [tools.tdep]() package developed by [Florian Knoop](). 
Look through the [tutorials]() if something is missing here. They are _very_ very well structured and thought out. A lot of the benchmarks I show here could be useful to try if you want to start fresh with TDEP calculations.
  



# sTDEP and sampling

sTDEP (stochastic temperature-dependent effective potential) is a powerful and efficient tool for calculating several lattice dynamics-related properties at finite temperatures. 

Non-technical summary:  
Phonopy displaces one atom at a time. sTDEP displaces all the atoms as they would vibrate at that particular temperature. I really like this summary picture that Olle Hellman showed us in his intro to TDEP presentation. 
<img width="773" alt="phonopy_vs_TDEP" src="https://github.com/NU-CEM/Group_wiki/assets/49740967/400b97a3-6140-47b8-94b9-9736ed1f7cbb">


For a longer technical summary check out the [manual]() or the [tutorial]() page. All the equations are there.    

## Starting a calculation
Every TDEP calculation requires two files: `infile.ucposcar` and `infile.ssposcar`. Generate the `infile.ssposcar` using the following command. It copies the resulting `outfile.ssposcar` to `infile.ssposcar`
```
generate_structure -na 64
cp outfile.ssposcar infile.ssposcar
```
Generate the displaced structures with the following command. For the first iteration 
```
canonical_configuration --quantum --maximum_frequency 20 --temperature 300 -n 1
```

## Things to converge  
["Converging things is annoying, but what can we do."](https://github.com/tdep-developers/tdep-tutorials/tree/main/01_sampling/convergence)     
`-na` while generating the canonical configuration. Tip:     
`-rc2` cutoff for harmonic force constant. Tip: check the `tdep_plot_fc_norms` first. A realspace cutoff is printed in the output. I generally go by this number.         
`-rc3` cutoff for third order force constant Tip: I usually half the harmonic cutoff here.       
r^2   
overdetermination ratio         
number of samples & iterations        

## Makefile 
A master file with all the commands from TDEP and tools.tdep useful for perforning sampling are collected here. Thankfully, Florian is an FHI-aims user so all the geometries created and parsed by the tools.tdep scripts are in the FHI-aims format by default 😄. Linking samples from a previous iteration through `tdep_ln_previous_samples` preconditions the self-consistent iteration which helps in faster convergence.   
```
rc2 = 10
rc3 = 5
temp = 200
iters = 8
link:
        tdep_ln_previous_samples      
postprocess: 
        tdep_parse_output samples/*/aims.out samples_prev/*/aims.out
        extract_forceconstants -rc2 $(rc2) -rc3 $(rc3) 2>&1 | tee extract_forceconstants.log
        ln -sf outfile.forceconstant infile.forceconstant
        ln -sf outfile.forceconstant_thirdorder infile.forceconstant_thirdorder
        phonon_dispersion_relations -p --dos
        tdep_plot_dos outfile.phonon_dos.hdf5 
        tdep_plot_dispersion outfile.dispersion_relations.hdf5 
        tdep_plot_fc_norms
iteration:
        tdep_create_next_iteration --max-samples $(iters) -T $(temp)                    
```
I would recommend looking at the output of `tdep_plot_fc_norms` to try and understand the interactions in your system. ["The bonds must be there."]() Make sure to change the `iters` tag after each iteration. 

# Thermodynamics


# Lineshape

Lineshape is needed to generate cool phonon bandstructures like [this]() and for determining the width of peaks in Raman and IR spectra.   
The `lineshape` program needs four input files: `infile.ucposcar`,`infile.ssposcar`,`infile.forceconstant`, and `infile.forceconstant_thirdorder`. Run the program using:
```
lineshape --highsymmetrypoint GM -qg 3 3 3 --temperature 100 
```
This will generate the lineshape at the Gamma point and 100K. To make 

# Raman 

# Other tips
You can get some inforamtion about your crystal structure using the following command. It also prints out information about the Brillouin zone.  
```
crystal_structure_info
```
To customize the path of the phonon bandstructure, an `infile.qpoints_dispersion` must be created. Here is an example: 
```
CUSTOM                      ! Bravais lattice type
  100                       ! Number of points on each path
   11                       ! Number paths between special points
 0.00000  0.00000  0.00000  -0.50000  0.50000  0.00000  GM  X
-0.50000  0.50000  0.00000  -0.50000  0.50000 -0.05002  X   Y
-0.50000  0.50000 -0.05002  -0.27501  0.27501 -0.27501  Y   S
-0.27501  0.27501 -0.27501   0.00000  0.00000  0.00000  S  GM
 0.00000  0.00000  0.00000   0.50000  0.50000 -0.50000  GM  Z
 0.50000  0.50000 -0.50000   0.27501  0.72499 -0.72499  Z   S1
 0.27501  0.72499 -0.72499   0.00000  0.50000 -0.50000  S1  N
 0.00000  0.50000 -0.50000  -0.25000  0.75000 -0.25000  N   P
-0.25000  0.75000 -0.25000   0.05002  0.94998 -0.50000  P   Y1
 0.05002  0.94998 -0.50000   0.50000  0.50000 -0.50000  Y1 Z
-0.50000  0.50000  0.00000  -0.25000  0.75000 -0.25000  X  P
```
To evalute the phonon freqauencies at these points run use the `-rp` tag. It stands for read path: 
```
phonon_dispersion_relations -rp -p --dos
```
