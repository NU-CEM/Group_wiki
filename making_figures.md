Setup [Blender](), [Beautiful Atoms]() and [ASE](). 

```
from ase.io import read
from batoms import Batoms
perov = read("/Users/w21013885/Downloads/BaZrS3/geometry.in")
perov = Batoms(label="perov",from_ase=perov)
```

```
perov.bond.settings[('Ba', 'S')].polyhedra = False
perov.bond.settings[('Zr', 'S')].max = 4.0
```
