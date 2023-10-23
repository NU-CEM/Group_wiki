This is a collection of my notes for the TDEP (temperature-dependent effective potential) method. Installation instructions are [here](https://github.com/NU-CEM/Group_wiki/blob/main/tdep_installation.md). Also, install the [tools.tdep](https://github.com/flokno/tools.tdep) package developed by [Florian Knoop](https://github.com/flokno). 
Look through the [tutorials](https://github.com/tdep-developers/tdep-tutorials) if something is missing here. They are _very_ very well structured and thought out. A lot of the benchmarks I show here could be useful to try if you want to start fresh with TDEP calculations.
  



# sTDEP

sTDEP (stochastic temperature-dependent effective potential) is a powerful and efficient tool for calculating several lattice dynamics-related properties at finite temperatures. 

Non-technical summary:  
Phonopy displaces one atom at a time. sTDEP displaces all the atoms as they would vibrate at that particular temperature. I really like this summary picture that [Olle Hellman](https://github.com/ollehellman) showed us in his intro to TDEP presentation. 
<img width="773" alt="phonopy_vs_TDEP" src="https://github.com/NU-CEM/Group_wiki/assets/49740967/400b97a3-6140-47b8-94b9-9736ed1f7cbb">

For a longer technical summary check out the [manual](https://tdep-developers.github.io/tdep/program/canonical_configuration/) or the [tutorial](https://github.com/tdep-developers/tdep-tutorials/tree/main/01_sampling) page. All the equations are there.    

I highlight two steps here:    
- starting a calculation, (generating input files, initial step)
- sampling (self-consistency loop, running DFT on displaced structures)

## Starting a calculation
Every TDEP calculation requires two files: `infile.ucposcar` and `infile.ssposcar`. Generate the `infile.ssposcar` using the following command. It copies the resulting `outfile.ssposcar` to `infile.ssposcar`
```
generate_structure -na 64
cp outfile.ssposcar infile.ssposcar
```
Generate the displaced structures with the following command. Only for the first iteration, one needs to use a `--maximum_frequency` tag. This is just a guess. For a FHI-aims geometry, I use the `--format_output 4` tag (default is VASP).   
```
canonical_configuration --quantum --maximum_frequency 20 --temperature 300 -n 1 --format_output 4
```
This will generate a `outfile.fakeforceconstant` file. One can use this to just plot the dispersion relations but I think this doesn't have much physical meaning. The `phonon_dispersion` program requires an `infile.forceconstant`. Use the following command:
```
ln -s outfile.fakeforceconstant infile.forceconstant
phonon_dispersion_relations -p
tdep_plot_dispersion outfile.dispersion_relations.hdf5 
```
For some reason, if you prefer plotting with gnuplot instead of python, the `phonon_dispersion_relations` program generates `outfile.dispersion_relations.gnuplot_pdf` file, replace the third command above with the following:
```
gnuplot outfile.dispersion_relations.gnuplot_pdf -p
```
## Sampling 



(TODO) update this with `infile.lotosplitting` to incorporate LO/TO splitting 

## Things to converge  
["Converging things is annoying, but what can we do."](https://github.com/tdep-developers/tdep-tutorials/tree/main/01_sampling/convergence)     
`-na` while generating the canonical configuration. Tip:     
`-rc2` cutoff for harmonic force constant. Tip: check the `tdep_plot_fc_norms` first. A realspace cutoff is printed in the output. I generally go by this number.         
`-rc3` cutoff for third order force constant Tip: I usually half the harmonic cutoff here.       
r^2   
overdetermination ratio         
number of samples & iterations        

## Makefile 
A master file with all the commands from TDEP and tools.tdep useful for performing sampling is collected here. Thankfully, Florian is an FHI-aims user so all the geometries are created and parsed by the tools.tdep scripts are in the FHI-aims format by default 😄. Linking samples from a previous iteration through `tdep_ln_previous_samples` preconditions the self-consistent iteration which helps in faster convergence.   
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
I would recommend looking at the output of `tdep_plot_fc_norms` to try and understand the interactions in your system. ["The bonds must be there."]() Make sure to change the `iters` tag after each iteration!


# Thermodynamics

To calculate the thermodynamic properties such as free energies, entropy, and heat capacity, phonon calculations are required. This is because the partition function depends on the frequencies of phonons and consequently, the density of states. I like this [blogpost](https://blog.cupcakephysics.com/thermodynamics%20and%20statistical%20physics/2015/10/04/thermodynamic-properties-of-the-quantum-harmonic-oscillator.html) that derives the thermodynamic properties of the quantum harmonic oscillator starting all the way from the partition function.   

The `-U0` tag along with the `extract_forceconstants` program provides the harmonic free energy and the $U_0$ correction until the fourth order. 
```
extract_forceconstants -rc2 10.0 -rc3 5 -U0
```
It will generate a file called `outfile.U0`. This file prints four numbers: average potential energy, $U_0$ correction at 2nd order, $U_0$ correction at 3rd order, $U_0$ correction at 4th order. Here is an example of outputs when different orders of force constants are extracted. 
```
extract_forceconstants -rc2 10.0 -U0
-0.846153407991E+05 -0.846153816929E+05 -0.846153816929E+05 -0.846153816929E+05
extract_forceconstants -rc2 10.0 -rc3 5 -U0
-0.846153407991E+05 -0.846153816929E+05 -0.846153817256E+05 -0.846153817256E+05
extract_forceconstants -rc2 10.0 -rc3 5 -rc4 3 -U0
-0.846153407991E+05 -0.846153816929E+05 -0.846153817256E+05 -0.846153818852E+05
```
Generate the harmonic free energy using the `--temperature` tag to the `phonon_dispersion_relations` program using the following command. 
```
phonon_dispersion_relations --dos --temperature 300
```
It will generate a file called `outfile.free_energy`. This file prints four numbers: temperature, harmonic free energy harmonic entropy, and heat capacity. 

To get the free energy corrected to an order, add the harmonic free energy (the second number in `outfile.free_energy`) to the nth order correction (nth number in `outfile.U0`). Here is an example of how the free energy with second order correction changes with the number of samples: (The system considered here is an RP phase at 300K) 

<img width="597" alt="free_energy_vs_number_of_samples" src="https://github.com/NU-CEM/Group_wiki/assets/49740967/cc690b98-f7f3-4cda-84fa-569c62730d3e">


# Lineshape

Lineshape is needed to generate cool phonon bandstructures like [this]() and for determining the width of peaks in Raman and IR spectra.   
The `lineshape` program needs four input files: `infile.ucposcar`,`infile.ssposcar`,`infile.forceconstant`, and `infile.forceconstant_thirdorder`. Run the program using:
```
lineshape --highsymmetrypoint GM -qg 3 3 3 --temperature 100 
```
This will generate the lineshape at the Gamma point and 100K. 


# Raman 


# IR 
(TODO) 
# Other tips
You can get some information about your crystal structure using the following command. It also prints out information about the Brillouin zone.  
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
To evaluate the phonon frequencies at these points, use the `-rp` tag. It stands for read path: 
```
phonon_dispersion_relations -rp -p --dos
```
Anharmoncity measure (TODO)
