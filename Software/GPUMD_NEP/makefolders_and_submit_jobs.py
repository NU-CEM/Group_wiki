import os
import ase.io

for i in range(1,281):
    structure =  ase.io.read('geometry.in-%03d'%i, format = 'aims')
    os.mkdir('calc_%03d'%i)
    os.chdir('calc_%03d'%i)
    os.system('cp ../geometry.in-%03d geometry.in'%i)
    os.system('cp ../aims.in aims.in')
    os.system('cp ../submit.sh .')
    os.system('sbatch submit.sh')
    os.chdir('../')
