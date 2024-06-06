import ase.io

count_Ba = 0 
count_Zr = 0 
count_S  = 0

atoms =  ase.io.read('aims.out')
chemical_formula = atoms.get_chemical_symbols()
total_energy = atoms.get_potential_energy()
Ba_energy = -225060.520483955 
Zr_energy = -197453.110828099/2
S_energy  = -347575.482257489/32
for j in chemical_formula:
    if 'Ba' in j:
        count_Ba += 1
    if 'Zr' in j:
        count_Zr += 1
    if 'S'  in j:
        count_S += 1
heat_of_formation = (total_energy-count_Ba*Ba_energy-count_Zr*Zr_energy-count_S*S_energy)
with open('aims.out', 'r') as file:
    filedata = file.read()
filedata = filedata.replace('| Total energy corrected        :', '| Total energy corrected        :  %s'%heat_of_formation)
with open('aims.out', 'w') as file:
    file.write(filedata)

