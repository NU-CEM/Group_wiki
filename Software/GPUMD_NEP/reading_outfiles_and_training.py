import numpy as np
from ase.build import bulk, make_supercell, surface
from ase.calculators.emt import EMT
from ase.io import write
from calorine.tools import relax_structure
from hiphive.structure_generation import generate_mc_rattled_structures

import ase

training_structures = []
count = 1
for i in range(1,2255):
    try:
        atoms = ase.io.read(f'calc_{i:04d}/aims/calculation/aims.out')
        if not atoms in training_structures:
             training_structures.append(atoms)
        count=count+1
    except:
        if FileNotFoundError:
            pass
from calorine.nep import setup_training

# prepare input for NEP construction
parameters = dict(version=4,
                  type=[3, 'Ba','Zr','S'],
                  cutoff=[8, 4],
                  neuron=30,
                  generation=1000000,
                  batch=10000000)
