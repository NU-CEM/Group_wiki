## FHI-aims: The basics

- There are only two main input files in aims, [geometry.in](./aims_demo/geometry.in) and [control.in](./aims_demo/control.in)
- The geometry.in file is the POSCAR analogue of VASP which contains the lattice parameters and atomic positions in Cartesian space. 
- The control.in file is the INCAR, KPOINTS and POTCAR combined. The file contains the DFT settings (functional and SCF convergence criteria) and kpoints and the atomic species files. 
- For production runs, species files are generally "tight" settings and can be internally tightened with the tight tier-1 or tight-deafult and tight tier-2 options. 
- Unlike VASP, input keywords/species in the control.in are insentive to ordering from the geometry.in files. The k-grids by default are Gamma-centered. 

In the species_default folder of the aims repo, there are different kinds of basis sets one can choose. These need to be `cat` into the control.in file for every unique atom type. The standard practice for solid state DFT is the default settings/folder(s). There is a are species_default > default_2010 basis sets which are now an outdated version. However these basis sets still produced fantastic agreement with experiment and can still be used for comparison. From now on, I will use species_default > default_2020 which is what the developers also recommend. 
Inside species_default > default_2020 there are light (generally only for testing), tight (generally used for production runs), very_tight and other folders which to my knowledge I haven't seen in use so far. 

## Troubleshooting:
If the your SCF does not converge or converges slowly, first try
```
sc_init_iter 10
```
This restarts the SCF with the unconverged density after the 10th cycle. Helps in converging problems when the k-grid sampling is not very dense. 
## Electronic band structure analysis 

1. Spin-orbit coupling: The keyword `include_spin_orbit non_self_consistent` must be included in the `control.in`. Aims prints both scalar-relativistic values and the spin-orbit-coupled values in band***.out files for each path segement.   

## Phonopy with FHI-aims
For finite displacement evaluation of the force constant matrix and other properties related to harmonic approximations, Phonopy with an aims interface can be used. Personally, I used to like the old integratability with one simple [phonopy-FHI-aims](https://th.fhi-berlin.mpg.de/sitesub/meetings/DFT-workshop-2016/uploads/Meeting/Tutorial_6_2016.pdf) script, but this script is now defunct. The new Phonopy version now has an [aims interface](https://phonopy.github.io/phonopy/interfaces.html) which is triggered by the `--aims` keyword. 

An excellent resource for VASP with Phonopy and Phono3py along with other tips is [here](https://www.slideshare.net/jmskelton/phonons-phonopy-pro-tips-2015). 

To perform a simple Phonopy calculation follow these steps, they are also listed by the developers [here](https://github.com/phonopy/phonopy/blob/develop/example/diamond-FHI-aims/README.md).

1. Create supercells with displacements. Standard dispplacement step is 0.01 Angstrom:
```
phonopy -d --dim="2 2 2" --aims
```
- If you are copying the same control.in folder from the one you used in the relaxation step, please make sure you have removed the `relax_geometry` keyword from the control.in. I have wasted many computer hours (oops) by making this mistake!!
- Please also keep in mind to scale your k-grids acoording to the supercell size. The general rule of thumb is to half the k-grids if the supercell is doubled, 1/3rd when the supercell is tripled and so on. The idea is to achieve the same k-grid sampling as in the unit cell. 
2. Copy the generated supercells into folders containing one `geometry.in` (rename!) and one `control.in`. The old scipt used to do this for the user, but now one has to do this on thier own (rolls eyes). The `control.in` should contain the `sc_accuracy forces` keyword. I have tested benchmarked this keyword in the [past](https://aip.scitation.org/doi/full/10.1063/5.0041717). This number should be tighter than the forces used in the relaxation. One must be careful at this point. The forces should have the same relative error with the displacement step size. Here's a [nicer explanation](https://www.tcm.phy.cam.ac.uk/castep/Phonons_Guide/Castep_Phononsch2.html). Now, run aims in each folder, each producing an aims outfile. 
3. Make the force constant matrix by collecting forces from all the outfiles in the folders we created. Out of habit, I still name my folders like the old script did. The 1st and the last folder need to be listed in this way `{first_folder..last_folder}` : 
```
phonopy -f phonopy-FHI-aims-displacement-{001..120}/outfile
```
4. **Post processing**:
- Plot the phonon band structure! First create a `band.conf` file which constains phonopy related keywords. To plot a bandstrcture, we need to specify a band path. Its almost become standard practice at this point to follow the convention set by [Setyawan et al.](https://doi.org/10.1016/j.commatsci.2010.05.010)  The high symmetry points sample the irreducible part of the Brillouin zone. `-p` is for plot and `-s` is for save. A sample band.conf is here. Note: Remember to symmetrize your forces by using the `FC_SYMMETRY = .TRUE.` keyword. This ensures translational symmetry and permutation symmetry is appiled on the force conatant matrix. This fixes tiny imaginary modes seen at the Gamma point. 
```
phonopy -p -s band.conf
```
- Plot the DOS. Make a `dos.conf` file for a total DOS evaluation. For partial DOS include `PDOS = 1 2, 3 4, 5 6` where inequivalent atoms are seperated by a comma. 
```
phonopy -p -s dos.conf
```
- Plot the thermal properteries which can be evaluated with the  `-t` argument. This is printed out on the terminal, so copy this into the a file. The same info is printed into a thermal.yaml file as well but (at the risk of sounding like a broken record, because of the old script) I like the formatting that is printed on the terminal so I save it in a file (personal preference).  Requires some formatting of the thermal.dat file (deleting the top few lines, no nig deal). 
```
phonopy -p -s -t dos.conf > thermal.dat 
```
