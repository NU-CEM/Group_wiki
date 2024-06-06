from ase.io import read
from calorine.calculators import CPUNEP

structure = read('geometry.in')
calc = CPUNEP('nep.txt')
structure.calc = calc

print('Energy (eV):', structure.get_potential_energy())
print('Forces (eV/Å):\n', structure.get_forces())
print('Stress (GPa):\n', structure.get_stress())
