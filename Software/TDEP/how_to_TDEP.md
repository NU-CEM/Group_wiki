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
`-na` while generating the canonical configuration. Tip: (TODO)     
`-rc2` cutoff for harmonic force constant. Tip: check the `tdep_plot_fc_norms` first. A realspace cutoff is printed in the output. I generally go by this number.         
`-rc3` cutoff for third order force constant Tip: I usually half the harmonic cutoff here.       
r^2     
<img width="597" alt="Screenshot 2023-10-25 at 12 04 52" src="https://github.com/NU-CEM/Group_wiki/assets/49740967/45ca346b-eb02-4ac8-a8ae-fecfc2346147">

overdetermination ratio. I don't fully understand this number yet, but here is how it varies with the number of iterations. In the tutorial, it recommended that this number be "in the 100s". Note: if you extract `-rc3` then there is an overdetermination ratio for this also. Here, I plot it for 2nd order.     
<img width="597" alt="Screenshot 2023-10-25 at 10 55 11" src="https://github.com/NU-CEM/Group_wiki/assets/49740967/036fdf00-8719-4470-adb6-82945fdc7350">

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

Note: if your system has imaginary modes, the free energy cannot be computed within the model Hamiltonian considered in TDEP. The free energy of a system blows up when there are imaginary modes (looks something ridiculous like 0.33594303423E+10 rather than something reasonable like 0.23147290181E-01). This is why I haven't plotted the free energy if $2^1$ in the plot above. It is the first iteration of the sTDEP, which has an imaginary mode. 

# Lineshape

Lineshape is needed to generate cool phonon bandstructures like [this](https://github.com/tdep-developers/tdep-tutorials/blob/main/05_lineshape/Figures/T100K_anh_bands_333.png) and for determining the width of peaks in Raman and IR spectra.   
The `lineshape` program needs four input files: `infile.ucposcar`,`infile.ssposcar`,`infile.forceconstant`, and `infile.forceconstant_thirdorder`. Run the program using the following command. If you use the `--readpath` tag for a custom path, the an `infile.qpoints_dispersion` is also required. 
```
mpirun -n 4 lineshape --readpath --path -qg 3 3 3 --temperature 100 
```
This will generate the lineshape at the Gamma point and 100K. Use this [script]() to plot the data to get something like the following. (These are results from an RP phase at 100K. Note the nice imaginary modes 😄)
<img width="597" alt="lineshape_100K" src="https://github.com/NU-CEM/Group_wiki/assets/49740967/b84a22cb-e29c-4170-a105-d4cc63dd8726">

# Raman 
With the sTDEP, one can get the peak positions([Phonopy-Spectroscopy](https://github.com/skelton-group/Phonopy-Spectroscopy) style by displacing atoms along Raman active modes and evaluate dielectric tensors) and the peak widths (by evaluating the spectral function at the Gamma point) to generate the Raman tensors. This program requires the `infile.ucposcar`     

Displaced structures are made using the following command. This generates the displaced structures along the eigenvectors in `outfile.ucposcar.mode.xxx.plus` and `utfile.ucposcar.mode.xxx.minus` files. Use this [script]() to generate the folders where you will run a DFT single-point calculation to calculate a dielectric tensor. 
```
tdep_displace_modes 
```
Generate the spectral functions using the following command. This will generate an `outfile.phonon_self_energy.hdf5`
```
lineshape --temperature 300 --qdirin 0 0 1
```
# IR 
(TODO) 

# Thermal conductivity 
(TODO)
# Other tips
You can get some information about your crystal structure using the following command. It also prints out information about the Brillouin zone.  
```
crystal_structure_info
```

| Program | Required input files |
| ------- | -------------------- |
|         |                      | 
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
# Anharmonicity measure
The [anharmonicity measure]()

<img width="597" alt="anharmonicity_measure_vs_temp" src="https://github.com/NU-CEM/Group_wiki/assets/49740967/6c41db73-08c5-45a5-92a7-441c0c6c79e9">


