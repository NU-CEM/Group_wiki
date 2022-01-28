## FHI-aims: The basics

- There are only two main input files in aims, geometry.in and control.in
- The geometry.in file is the POSCAR analogue of VASP which contains the lattice parameters and atomic positions in Cartesian space. 
- The control.in file is the INCAR, KPOINTS and POTCAR combined. The file contains the DFT settings (functional and SCF convergence criteria) and kpoints and the atomic species files. 
- For production runs, species files are generally "tight" settings and can be internally tightened with the tight tier-1 or tight-deafult and tight tier-2 options. 
- Unlike VASP, input keywords/species in the control.in are insentive to ordering from the geometry.in files. The k-grids by default are Gamma-centered. 

## Phonopy with FHI-aims
For finite displacement evaluation of the force constant matrix, Phonopy can be interfaced with aims. Personally, I used to like the old integratability with one simple [phonopy-FHI-aims][https://th.fhi-berlin.mpg.de/sitesub/meetings/DFT-workshop-2016/uploads/Meeting/Tutorial_6_2016.pdf] script, but this script is now defunct. The new Phonopy version now has an [aims interface](https://phonopy.github.io/phonopy/interfaces.html) which is triggered by the `--aims` keyword. 

To perform a simple Phonopy calulation follow these steps, they are also listed by the developers [here](https://github.com/phonopy/phonopy/blob/develop/example/diamond-FHI-aims/README.md)

1. Create supercells with displacements. Standard dispplacement step is 0.01 Angstrom:
```
phonopy -d --dim="2 2 2" --aims
```
- If you are copying the same control.in folder from the one you used in the relaxation step, please make sure you have removed the `relax_geomtry` keyword from the control.in. I have wasted many computer hours (oops) by making this mistake!!
- Please also keep in mind to scale yur k-grids acoording to the supercell size. The general rule of thumb is to half the k-grids if the supercell is doubled, 1/3rd when the supercell is tripled and so on. The idea is to achieve the same k-grid sampling as in the unit cell. 
2. Copy the generated supercells into folders containing one `geometry.in` (rename!) and one `control.in`. The old scipt used to do this for the user, but now one has to do this on thier own (rolls eyes). The `control.in` should contain the `sc_accuracy forces` keyword. I have tested benchmarked this keyword in the [past](https://aip.scitation.org/doi/full/10.1063/5.0041717). This number should be tighter than the forces used in the relaxation. One must be careful at this point. The forces should have the same relative error with the displacement step size. Here's a [nicer explanation](https://www.tcm.phy.cam.ac.uk/castep/Phonons_Guide/Castep_Phononsch2.html). Now, run the aims in each folder, producing an aims outfile. 
3. Make the force constant matrix by collecting forces from all the outfiles in the folders we created. Out of habit, I still name my folders like the old script did. The 1st and the last folder need to be listed in this way `{first_folder..last_folder}`. : 
```
phonopy -f phonopy-FHI-aims-displacement-{001..120}/outfile
```
4. Plot the phonon band structure!
```
phonopy -p -s band.conf
```
