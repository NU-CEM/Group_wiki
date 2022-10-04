# Crystal Structure

Setup [Blender](https://www.blender.org/), [Beautiful Atoms](https://beautiful-atoms.readthedocs.io/en/latest/index.html) and [ASE](https://wiki.fysik.dtu.dk/ase/index.html). 
To generate this following image, on the python interactive console type:

```
from ase.io import read
from batoms import Batoms
perov = read("/Users/w21013885/Downloads/BaZrS3/geometry.in")
perov = Batoms(label="perov",from_ase=perov)
```
On Batoms select "Polyhedral", "crystal_view", and "wrap". I'm sure there is a command line way of doing this, I don't know how to do that at the moment. 
```
perov.bond.settings[('Ba', 'S')] = False
perov.bond.settings[('Ba', 'S')].polyhedra = False
perov.bond.settings[('Zr', 'S')].max = 4.0
perov.polyhedra.settings["Zr"].color = [0.5799999833106995, 0.878000020980835, 0.878000020980835, 0.5]
```
On Render select "Attach Render" and on Viewport type: 1.0 0.0 1.0. 

# Phonon Bandstructure

There are several plotters that can be used for plotting a phonon BS. Unfortunately, at the moment, most require a VASP + Phonopy setup. There is aimstools which can be used, but it requires a FHI-aims + FHI-vibes + Phonopy setup. I found this [useful script written by Warda Rahim](https://github.com/warda-rahim/phononplotter/blob/master/phonon.py) and modified it [here]() (very tiny bit). It only requires a band.yaml file as an input which removes any dependance of electronic code. To run it :

```
python phonon.py -b band.yaml
```



# Electronic Bandstructure
