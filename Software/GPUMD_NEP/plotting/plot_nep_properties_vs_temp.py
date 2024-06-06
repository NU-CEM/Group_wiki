from calorine.gpumd import read_thermo
from dynasor.tools.acfs import smoothing_function
import matplotlib.pyplot as plt
import numpy as np
from scipy import constants
df = read_thermo('thermo.out')
k_B = constants.physical_constants["Boltzmann constant in eV/K"][0]

window_average = 100
df['potential_energy'] = df['potential_energy']/20000
df['potential_energy'] = df['potential_energy'] + 1.81440132003
df['potential_energy'] = df['potential_energy'] - (1.5*k_B*df['temperature'])

df['temperature'] = smoothing_function(df['temperature'], window_average)
df['potential_energy'] = smoothing_function(df['potential_energy'], window_average)

a = np.sqrt(df['cell_xx']**2+df['cell_xy']**2+df['cell_xz']**2)/10
a = smoothing_function(a, window_average)
b = np.sqrt(df['cell_yx']**2+df['cell_yy']**2+df['cell_yz']**2)/10
b = smoothing_function(b, window_average)
c = np.sqrt(df['cell_zx']**2+df['cell_zy']**2+df['cell_zz']**2)/10
c = smoothing_function(c, window_average)


k_B = constants.physical_constants["Boltzmann constant in eV/K"][0]

fig, axes = plt.subplots(figsize=(8.0, 6.0), nrows=2,sharex=True, dpi=120)
ax = axes
ax.plot(df.temperature,a/np.sqrt(2), label='a', color='#ffa5a5')
ax.plot(df.temperature,b/(2),label='b', color='#9f3434')
ax.plot(df.temperature,c/np.sqrt(2),label='c', color='#510000')
ax.legend()
ax.set_ylabel('Lattice parameter (A)')

ax = axes[1]
ax.plot(df.temperature,df.potential_energy, label = 'heating' , color = '#9f3434')
ax.set_ylabel('Energy (eV/atom)')
ax.set_xlabel('Temperature (K)')

plt.tight_layout()
plt.xlim(0,800)
plt.savefig('heating.png')
