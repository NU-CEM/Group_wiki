import os
from calorine.gpumd.io import write_xyz
import ase

atoms = ase.io.read('BaZrS3_conventional.in', format = 'aims')
atoms = atoms*10
write_xyz('model.xyz',atoms)
training_structures.append(atoms)
