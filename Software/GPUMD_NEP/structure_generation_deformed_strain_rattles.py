import numpy as np
from ase.build import bulk, make_supercell, surface
from ase.calculators.emt import EMT
from ase.io import write
from calorine.tools import relax_structure
from hiphive.structure_generation import generate_mc_rattled_structures
import ase

prototype_structures = {}
prototype_structures['Ba2ZrS4']   = ase.io.read("Ba2ZrS4_geometry.in", format='aims')
prototype_structures['Ba3Zr2S7']  = ase.io.read("Ba3Zr2S7_geometry.in", format='aims')
prototype_structures['Ba4Zr3S10'] = ase.io.read("Ba4Zr3S10_geometry.in", format='aims')

def generate_strained_structure(prim, strain_lim):
    strains = np.random.uniform(*strain_lim, (3, ))
    atoms = prim.copy()
    cell_new = prim.cell[:] * (1 + strains)
    atoms.set_cell(cell_new, scale_atoms=True)
    return atoms


def generate_deformed_structure(prim, strain_lim):
    R = np.random.uniform(*strain_lim, (3, 3))
    M = np.eye(3) + R
    atoms = prim.copy()
    cell_new = M @ atoms.cell[:]
    atoms.set_cell(cell_new, scale_atoms=True)
    return atoms


# parameters
strain_lim = [-0.05, 0.05]
n_structures = 30

training_structures = []
for name, prim in prototype_structures.items():
    for it in range(n_structures):
        prim_strained = generate_strained_structure(prim, strain_lim)
        prim_deformed = generate_deformed_structure(prim, strain_lim)

        training_structures.append(prim_strained)
        training_structures.append(prim_deformed)

n_structures = 5
rattle_std = 0.04
d_min = 2.4
n_iter = 20

size_vals = {}
size_vals['Ba2ZrS4'] = [(2, 2, 2), (3, 3, 3), (2, 2, 3), (2, 3, 2), (3, 2, 2)]
size_vals['Ba3Zr2S7'] = [(2, 2, 2), (3, 3, 3), (2, 2, 3), (2, 3, 2), (3, 2, 2)]
size_vals['Ba4Zr3S10'] = [(2, 2, 2), (3, 3, 3), (2, 2, 3), (2, 3, 2), (3, 2, 2)]
for name, prim in prototype_structures.items():
    for size in size_vals[name]:
        for it in range(n_structures):
            supercell = generate_strained_structure(prim.repeat(size), strain_lim)
            rattled_supercells = generate_mc_rattled_structures(supercell, n_structures=1, rattle_std=rattle_std, d_min=d_min, n_iter=n_iter)
            training_structures.extend(rattled_supercells)
print('Number of training structures:', len(training_structures))
count = 0
for atoms in training_structures:
    count = count + 1
    ase.io.write(f'geometry.in-{count:03d}', atoms, scaled=True, format = 'aims')
