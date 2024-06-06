import numpy as np
from ase.io import read
from calorine.calculators import CPUNEP
from calorine.tools import get_force_constants, relax_structure
from matplotlib import pyplot as plt
from pandas import DataFrame
from phonopy.units import THzToCm
from seekpath import get_explicit_k_path
import spglib

materials = ['BaZrS3_I4_mcm.in', 'BaZrS3_P4_mbm.in', 'BaZrS3_Pm3m.in', 'BaZrS3_Pnma.in']
for mater in materials:	
    structure = read(f'{mater}')
    calculator = CPUNEP('nep.txt')
    structure.calc = calculator
    print('before relax ', spglib.get_spacegroup(structure))
    relax_structure(structure, fmax=0.0001)
    print('after relax ', spglib.get_spacegroup(structure,symprec=1e-4))
    
    phonon = get_force_constants(structure, calculator, [4, 4, 4])
    structure_tuple = (structure.cell, structure.get_scaled_positions(), structure.numbers)
    
    path = get_explicit_k_path(structure_tuple)
    phonon.run_band_structure([path['explicit_kpoints_rel']])
    band = phonon.get_band_structure_dict()
    
    df = DataFrame(band['frequencies'][0])
    df.index = path['explicit_kpoints_linearcoord']
    
    fig, ax = plt.subplots(figsize=(4.2, 3), dpi=140)
    
    for col in df.columns:
        ax.plot(df.index, df[col], color='cornflowerblue')
    ax.set_xlim(df.index.min(), df.index.max())
    
    ax.set_ylabel('Frequency (THz)')
    ax2 = ax.twinx()
    ax2.set_ylabel('Frequency (cm$^{-1}$)')
    ax2.set_ylim(THzToCm * np.array(ax.get_ylim()))
    
    # beautify the labels on the x-axis
    labels = path['explicit_kpoints_labels']
    labels = ['$\Gamma$' if m == 'GAMMA' else m for m in labels]
    labels = [m.replace('_', '$_') + '$' if '_' in m else m for m in labels]
    df_path = DataFrame(dict(labels=labels,
                             positions=path['explicit_kpoints_linearcoord']))
    df_path.drop(df_path.index[df_path.labels == ''], axis=0, inplace=True)
    ax.set_xticks(df_path.positions)
    ax.set_xticklabels(df_path.labels)
    for xp in df_path.positions:
        ax.axvline(xp, color='0.8')
    
    plt.tight_layout()
    plt.savefig(f'{mater}_NEP_phonons.png')
    
    phonon.run_mesh(140)
    phonon.run_total_dos(freq_min=-3, freq_max=13, freq_pitch=0.02)
    dos = phonon.get_total_dos_dict()
    
    fig, ax = plt.subplots(figsize=(4.2, 3), dpi=140)
    
    ax.plot(dos['frequency_points'], dos['total_dos'])
    ax.set_xlabel('Frequency (THz)')
    ax.set_ylabel('Density of states')
    
    plt.tight_layout()
    plt.savefig(f'{mater}_NEP_DOS.png')
