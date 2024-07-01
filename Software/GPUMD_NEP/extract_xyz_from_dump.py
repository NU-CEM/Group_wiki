import os
import random
import ase.io
import numpy as np

def create_split_files():
    temperatures = [10, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000,1050,1100,1150]
    file_count = 1
    for temps in temperatures:
        os.chdir('temp_%04d'%temps)
        lines = open('dump.xyz').readlines()
        random_numbers = random.sample(range(500, 1000), 2)
        count = 1
        for i,line in enumerate(lines):
            if len(line.split())== 1:
                count = count +1
                if count in random_number:
                    number_of_atoms = int(line)
                    for iters in range(number_of_atoms+2):
                        with open('structure_%04d.xyz'%count,'a+') as split_xyz:
                            split_xyz.write(lines[iters].strip())
                            split_xyz.write('\n')
                    structure = ase.io.read("structure_%04d.xyz"%count)
                    ase.io.write('geometry.in',structure,format='aims',scaled=True)
                    os.system('cp geometry.in /home/mmm0117/NEP_ZrS2_v1/MD_sample_structures/geometry.in-%03d'%file_count)
                    file_count += 1
                    
        print('temperature %04d completed'%temps)
        os.chdir('../')

create_split_files()
    
